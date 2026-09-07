<p align="center"><img src="assets/header.svg" width="100%"></p>

<p align="center">
  <a href="https://www.nber.org/papers/w34910"><img alt="NBER" src="https://img.shields.io/badge/NBER-w34910-263657?style=for-the-badge"></a>
  <a href="https://doi.org/10.3386/w34910"><img alt="DOI" src="https://img.shields.io/badge/DOI-10.3386%2Fw34910-506A92?style=for-the-badge"></a>
  <a href="presentation.pdf"><img alt="Beamer corto" src="https://img.shields.io/badge/Beamer-4_slides-DCA54A?style=for-the-badge&logo=latex&logoColor=white"></a>
  <a href="extra/presentation-long.pdf"><img alt="Beamer largo" src="https://img.shields.io/badge/Beamer-largo-B64C4C?style=for-the-badge&logo=latex&logoColor=white"></a>
</p>

<p align="center">
  <a href="presentation.tex"><img alt="Fuente LaTeX" src="https://img.shields.io/badge/source-LaTeX-008080?style=flat-square&logo=latex&logoColor=white"></a>
  <a href="sim.py"><img alt="Auditoría SymPy" src="https://img.shields.io/badge/audit-SymPy-3B5526?style=flat-square&logo=sympy&logoColor=white"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-263657?style=flat-square"></a>
</p>

<p align="center">
  <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white">
  <img alt="Beamer" src="https://img.shields.io/badge/Beamer-506A92?style=flat-square&logo=latex&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="SymPy" src="https://img.shields.io/badge/SymPy-3B5526?style=flat-square&logo=sympy&logoColor=white">
  <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white">
</p>

# Repository 4 — Acemoglu, Kong & Ozdaglar (2026)

> **Daron Acemoglu, Dingwen Kong y Asuman Ozdaglar.** *AI, Human Cognition and Knowledge Collapse*. NBER Working Paper 34910, 20 de febrero de 2026. Working paper del NBER **sin arbitraje**, con varias versiones en circulación. Esta auditoría usa exclusivamente el PDF fechado 20-02-2026 (portada, p. 1 del PDF); la revisión de mayo no se usa como fuente del modelo.

## Pregunta y mecanismo

¿Puede una IA agéntica mejorar la decisión individual hoy y, al sustituir aprendizaje humano, destruir el conocimiento general que hace útiles esas recomendaciones mañana?

El mecanismo único combina dos aciertos complementarios: conocimiento general y conocimiento específico al contexto. El esfuerzo produce una señal privada y una contribución pública no internalizada; la IA agéntica añade precisión solo a la señal privada en el modelo base (sección 3.1, pp. 8–11 del PDF).

La heterogeneidad primitiva y tecnológica relevante es:

- $\theta_t$: **estado común**, random walk con innovación $\Sigma^2$;
- $\theta_{i,t}$: **estado idiosincrático**, i.i.d. $N(0,\sigma^2)$;
- $X_t$: **precisión pública heredada**;
- $Y_{i,t}=\sigma^{-2}+\lambda_Ie_{i,t}+\tau_A$: **precisión idiosincrática**;
- $\lambda_G,\lambda_I>0$: productividad informativa del esfuerzo; $I\in[1,M]$: escala de agregación; $\tau_A\ge0$: precisión de la IA agéntica; $\alpha>1$: curvatura del costo (secciones 3.1–3.2, pp. 8–12).

## Problema del agente

Dados $X_t$ y $\tau_A$, la elección estática es $e_{i,t}\ge0$:

$$
\max_{e_{i,t}\ge0}\ U_{i,t}=f(0,0)+G(X_t)\Delta_G
+G(X_t)G(Y_{i,t})\Delta_X-\frac{e_{i,t}^{\alpha}}{\alpha},
\quad Y_{i,t}=\sigma^{-2}+\lambda_Ie_{i,t}+\tau_A.
$$

Aquí $G(\tau)=2\Phi(\sqrt\tau)-1$ y $g=G'$. La CPO interior es

$$
\Delta_XG(X_t)\lambda_Ig(\sigma^{-2}+\lambda_Ie_{i,t}+\tau_A)
=e_{i,t}^{\alpha-1}.
$$

$f$ es débilmente creciente, $\Delta_G+\Delta_I+\Delta_X=1$ y el paper impone **Assumption 1:** $\Delta_I=0$, $\Delta_X>0$. Como $g$ decrece y $e^{\alpha-1}$ crece para $\alpha>1$, la utilidad es estrictamente cóncava y el máximo es único y finito; es interior si $X_t>0$, mientras que $e^*=0$ si $X_t=0$ (ecuaciones (4)–(6), secciones 3.3–3.5, pp. 12–15).

## Observación 1

**Observación 1.** Bajo $\Delta_I=0$, $\Delta_X>0$, $\lambda_I>0$, $\alpha>1$, $e_{i,t}\ge0$, $\tau_A\ge0$, precisiones gaussianas y $X_t,Y_{i,t}>0$ para que las derivadas sean finitas,

$$
\frac{\partial^2U_{i,t}}{\partial e_{i,t}\partial X_t}
=\Delta_X\lambda_Ig(X_t)g(Y_{i,t})>0,
\qquad
\frac{\partial^2U_{i,t}}{\partial e_{i,t}\partial\tau_A}
=\Delta_XG(X_t)\lambda_Ig'(Y_{i,t})<0.
$$

La primera desigualdad usa complementariedad productiva y $g>0$; la segunda usa rendimientos decrecientes de precisión, $g'<0$. Por monotone comparative statics, $e(X,\tau_A)$ sube con $X$ y cae con $\tau_A$, estrictamente para $X>0$ (Observaciones 1–2, sección 3.4–3.5, pp. 13–15).

## Observación 1, revisada

El objeto es la **diferencia cruzada de la utilidad privada estática** respecto del esfuerzo y una precisión, no el bienestar social ni la dinámica de $X_t$. La estática comparativa de “precisión de IA” es respecto de $\tau_A$, no de $\alpha$, que en el PDF denota la curvatura del costo.

Bajo gaussianidad, $X_t>0$, $Y_{i,t}>0$, $\lambda_I>0$, $\Delta_X>0$, costo convexo y **Assumption 1**:

- la complementariedad $X$–esfuerzo es estricta en el interior;
- la sustitución $\tau_A$–esfuerzo es estricta solo si $X_t>0$; en $X_t=0$, $G(0)=0$, el esfuerzo óptimo es cero para toda $\tau_A$;
- ninguna desigualdad demuestra por sí sola “colapso”: eso requiere la ley de movimiento (7), atomisticidad, externalidad no internalizada y elasticidad $1/(\alpha-1)>4$ para estabilidad local de cero (Lemma 2, pp. 17–18);
- si $\Delta_I>0$, el retorno privado al esfuerzo conserva el término $\Delta_I\lambda_Ig(Y)$ aun cuando $X=0$; por tanto, el colapso literal deja de seguir del argumento.

La condición omitida en el enunciado estricto es **$X_t>0$**: aparece recién en la nota 4 tras la CPO (p. 15), donde el paper reconoce que en $X_t=0$ el retorno y el esfuerzo son cero. Además, la fórmula de la primera derivada cruzada, inmediatamente después de la Observación 1 (p. 14), no está definida como derivada finita en $X_t=0$ porque $g(X)\to\infty$ al acercarse a cero. El resultado correcto es interior; el orden global débil puede formularse con diferencias crecientes.

La objeción económica más fuerte no es que el paper ignore toda producción de IA: §§5.1–5.2 sí la relajan. Precisamente, con precisión sintética $\tau_{syn}>0$, $F_{syn}(0)>0$ y el propio paper reemplaza el colapso por un estado de conocimiento bajo estrictamente positivo (ecuaciones (12)–(13), Proposición 15, pp. 31–32). El “colapso total” es, por tanto, un resultado conjunto de $\Delta_I=0$ y flujo autónomo nulo, no una consecuencia general de recomendaciones precisas.

## Reproducción

```bash
python -m pip install -r requirements.txt
python sim.py
lualatex presentation.tex
lualatex extra/presentation-long.tex
```

`sim.py` verifica simbólicamente la CPO y la descomposición de $\partial\bar U^+/\partial\tau_A$, imprime un tramo numérico reproducible donde el bienestar cae y regenera [`welfare-accuracy.pdf`](extra/figures/welfare-accuracy.pdf) y [`welfare-accuracy.png`](extra/figures/welfare-accuracy.png).

## Estructura

```text
.
├── assets/
│   ├── header.svg
│   └── acemoglu-beamer.sty
├── extra/
│   ├── figures/
│   │   ├── welfare-accuracy.pdf
│   │   └── welfare-accuracy.png
│   ├── presentation-long.pdf
│   └── presentation-long.tex
├── hand/
│   ├── README.md
│   └── manual-verification.jpg
├── paper/
│   ├── README.md
│   └── w34910.pdf        # solo local; ignorado por git
├── presentation.pdf
├── presentation.tex
├── README.md
├── extensions.md
├── prompts.md
├── sim.py
├── requirements.txt
├── LICENSE
└── .gitignore
```

La comprobación manuscrita de la estudiante está en [`hand/manual-verification.jpg`](hand/manual-verification.jpg); el repositorio no inventa esa evidencia.

## Referencia

Acemoglu, D., Kong, D., & Ozdaglar, A. (2026). *AI, Human Cognition and Knowledge Collapse*. NBER Working Paper 34910. <https://doi.org/10.3386/w34910>
