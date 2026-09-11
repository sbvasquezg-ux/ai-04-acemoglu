#!/usr/bin/env python3
"""Audit the static FOC and steady-state welfare in AKO (2026, Feb. 20)."""
from pathlib import Path
import math
import os
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", "/tmp/ai04-matplotlib")
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
FIG = ROOT / "extra" / "figures"

def symbolic_checks():
    e, X, tau, sig, lam, DX, a = sp.symbols("e X tau sig lam DX a", positive=True)
    G = sp.Function("G")
    Y = sig + lam*e + tau
    U = G(X)*DX + G(X)*G(Y)*DX - e**a/a
    foc = sp.diff(U, e)
    expected = DX*G(X)*lam*sp.Subs(sp.Derivative(G(sp.Symbol("z")), sp.Symbol("z")), sp.Symbol("z"), Y) - e**(a-1)
    assert sp.simplify(foc-expected) == 0
    DG, GX, GY, gX, gY, Xp, ep = sp.symbols(
        "Delta_G G_X G_Y g_X g_Y Xprime eprime", real=True
    )
    # Total derivative before imposing the private FOC. Y'=1+lambda*e'.
    total = gX*Xp*(DG+GY*DX) + GX*DX*gY*(1+lam*ep) - e**(a-1)*ep
    foc_rhs = DX*GX*lam*gY
    envelope = sp.simplify(total.subs(e**(a-1), foc_rhs))
    expected_envelope = GX*DX*gY + gX*Xp*(DG+GY*DX)
    assert sp.simplify(envelope-expected_envelope) == 0

def G(z):
    if z <= 0: return 0.0
    return math.erf(math.sqrt(z/2.0))

def g(z):
    return math.exp(-z/2.0)/math.sqrt(2*math.pi*z)

def bisect(fun, lo, hi, n=100):
    flo = fun(lo)
    for _ in range(n):
        mid=(lo+hi)/2; fm=fun(mid)
        if flo*fm <= 0: hi=mid
        else: lo=mid; flo=fm
    return (lo+hi)/2

def steady_high(tau, p):
    alpha, dX, lI, lG, island, sigp, Sigma2 = p
    def W(e):
        q=lG*island*e
        return 0.5*q*(math.sqrt(1+4/(Sigma2*q))-1) if q>0 else 0.0
    def D(e):
        return dX*G(W(e))*lI*g(sigp+lI*e+tau)-e**(alpha-1)
    grid=np.geomspace(1e-12,100,3000)
    roots=[]
    last=grid[0]; fl=D(last)
    for z in grid[1:]:
        fz=D(z)
        if fl*fz<0: roots.append(bisect(D,last,z))
        last=z; fl=fz
    e=max(roots) if roots else 0.0
    return W(e), e

def numerical_counterexample():
    # alpha, Delta_X, lambda_I, lambda_G, I, sigma^-2, Sigma^2
    p=(2.0,0.8,1.0,1.0,12.0,0.5,1.0); dG=0.2
    taus=np.linspace(0,16,321); welfare=[]; stocks=[]
    for tau in taus:
        X,e=steady_high(tau,p); Y=p[5]+p[2]*e+tau
        welfare.append(G(X)*dG+G(X)*G(Y)*p[1]-e**p[0]/p[0]); stocks.append(X)
    welfare=np.array(welfare); stocks=np.array(stocks)
    k=int(np.argmax(welfare))
    # Explicit reproducible decreasing segment.
    i,j=200,280
    assert welfare[j] < welfare[i]
    FIG.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11})
    fig,ax=plt.subplots(figsize=(7.4,4.2),constrained_layout=True)
    ax.plot(taus,welfare,color="#263657",lw=2.5,label=r"$\bar U^+$: utilidad neta de largo plazo")
    ax.axvspan(taus[0],taus[k],color="#506A92",alpha=.08)
    ax.axvspan(taus[k],taus[-1],color="#B64C4C",alpha=.07)
    ax.axvline(taus[k],color="#DCA54A",ls="--",label=rf"máximo: $\tau_A={taus[k]:.2f}$")
    ax.scatter([taus[i],taus[j]],[welfare[i],welfare[j]],color="#B64C4C",zorder=3)
    ax.annotate("efecto directo domina\nmejor consejo aumenta utilidad",
                xy=(.45*taus[k], welfare[int(.45*k)]), xytext=(2.2,.36),
                fontsize=9, color="#263657", ha="center",
                arrowprops={"arrowstyle":"->","color":"#506A92"})
    ax.annotate("efecto indirecto domina\nmenos esfuerzo reduce conocimiento general",
                xy=(taus[j],welfare[j]), xytext=(10.4,.29),
                fontsize=9, color="#B64C4C", ha="center",
                arrowprops={"arrowstyle":"->","color":"#B64C4C"})
    ax.set(xlabel=r"Eje horizontal: precisión de la recomendación de IA, $\tau_A$",
           ylabel=r"Eje vertical: utilidad estacionaria, $\bar U^+$",
           title="La precisión ayuda primero y perjudica cuando desplaza demasiado esfuerzo")
    ax.grid(alpha=.22); ax.spines[["top","right"]].set_visible(False); ax.legend(frameon=False)
    fig.savefig(FIG/"welfare-accuracy.pdf",bbox_inches="tight")
    fig.savefig(FIG/"welfare-accuracy.png",dpi=220,bbox_inches="tight")
    plt.close(fig)
    return taus[k],taus[i],welfare[i],taus[j],welfare[j]

if __name__ == "__main__":
    symbolic_checks()
    peak,t1,w1,t2,w2=numerical_counterexample()
    print("SymPy checks: PASS")
    print(f"Numerical counterexample: W({t1:.1f})={w1:.6f} > W({t2:.1f})={w2:.6f}")
    print(f"Grid welfare maximizer: tau_A={peak:.3f}")
    print(f"Figures: {FIG/'welfare-accuracy.pdf'} and {FIG/'welfare-accuracy.png'}")
