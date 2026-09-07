# Auditoría, cautelas y extensiones

## 1. La estática es privada; el daño es dinámico

La CPO de §3.5 maximiza utilidad de una cohorte corta tomando $X_t$ como dado. La contribución individual al conocimiento público es infinitesimal y no genera retorno privado (pp. 10 y 15). Por ello, información adicional no perjudica estáticamente al decisor, pero puede bajar $X_{t+1}$ mediante menor esfuerzo. Confundir estos objetos borra la externalidad que hace todo el trabajo.

## 2. Bienestar: no se “aplana”, cae

El paper mide bienestar como utilidad esperada de una cohorte representativa en estado estacionario, relativa a $f(0,0)$:

$$
\bar U=G(\bar X)\Delta_G+G(\bar X)G(\bar Y)\Delta_X-\bar e^\alpha/\alpha.
$$

No es utilidad descontada ni suma intergeneracional; transiciones finitas tampoco pesan en el criterio de largo plazo de §4.5 (ecuación (10), pp. 24 y 29). La derivada de §4.3 es

$$
\frac{\partial\bar U^+}{\partial\tau_A}
=\underbrace{g(\bar Y_h)G(\bar X_h)\Delta_X}_{DE\ge0}
+\underbrace{\frac{\partial G(\bar X_h)}{\partial\tau_A}
(\Delta_G+G(\bar Y_h)\Delta_X)}_{-IE\le0}.
$$

Con Assumption 2, las Proposiciones 10–11 muestran aumento estricto antes de $\tau_A^\star$ y caída estricta después; en el régimen múltiple el bienestar salta a cero al cruzar $\tau_A^c$ (pp. 26–27). El valor de opción de preservar conocimiento y la distribución entre agentes no entran: el objeto es una cohorte representativa ya en el steady state.

## 3. Casos límite

- $\tau_A\to\infty$: en el régimen único, $\bar U^+\to0$ (Proposición 10(iii), p. 27).
- $X_1=0$: $e=0$ y el sistema queda en cero en el baseline (nota 4, p. 15; ecuación (9), p. 17).
- $I$ grande: $\tau_A^c$ y $\tau_A^\star$ crecen solo como $\log I$; su razón converge a $1/\alpha$ (Proposición 12, p. 28).
- Elasticidad frontera $1/(\alpha-1)=4$: Lemma 2 solo cubre desigualdades estrictas. La igualdad no queda clasificada por el argumento asintótico (p. 18).
- $\tau_{syn}>0$: $F_{syn}(0)>0$; desaparece el estado cero y queda uno bajo pero positivo (Proposición 15, p. 32).

## 4. Seis candidatos a objeción

1. **IA y conocimiento general.** Sí se relaja: $I(\tau_A)=I_0+\exp(\eta\tau_A)$ en §5.1. Si $\eta<1/[2(\alpha-1)]$, el canal de sustitución aún domina asintóticamente; fuera de esa región la proposición no autoriza afirmar colapso (Proposición 14, pp. 30–31).
2. **Precisión exógena.** El baseline mantiene $\tau_A$ exógena. Con $\tau_A=\tau_A(X)$ y $\tau_A'(X)>0$, el mapa es $F(X;e[X,\tau_A(X)])$: el efecto total sobre esfuerzo combina $e_X>0$ y $e_{\tau}<0$; el signo requiere $e_X+e_{\tau}\tau_A'(X)$. La retroalimentación puede amortiguar o intensificar la caída, no garantiza por sí sola eliminar cero.
3. **Sustitución productiva fija.** El paper no usa CES: usa una tabla binaria y fija $\Delta_I=0$, $\Delta_X>0$ (Assumption 1, p. 9). Una CES no es una relajación anidada sin redefinir el problema de acierto binario; queda como extensión pendiente, no como resultado demostrado.
4. **Agregación exógena.** $I$ es paramétrica en el baseline y dependiente de IA en §5.1, pero no hay precio, entrada ni productor privado de conocimiento general. La atomisticidad elimina por construcción el retorno privado a la señal pública (p. 10).
5. **Heterogeneidad.** El equilibrio se restringe a islas y agentes simétricos (pp. 11–12). Con costos heterogéneos, basta una masa positiva con esfuerzo para que la precisión pública sea positiva; si esa masa no desaparece cerca de $X=0$, el colapso total no sigue. La magnitud exige especificar la distribución.
6. **Aprendizaje al usar IA.** No hay transición de habilidad individual: cada cohorte vive un período y $\theta_{i,t}$ es i.i.d. (pp. 8 y 13). Quispe y Xu (2026) reportan expansión persistente del portafolio de lenguajes incluso al excluir commits coescritos por el agente; es evidencia compatible con aprendizaje/complementariedad, aunque su adopción voluntaria impide una contradicción causal definitiva. Este canal añadiría un stock humano persistente que el baseline excluye.

## 5. Veredicto

Sobrevive un resultado condicional robusto: recomendaciones contextuales que reducen el esfuerzo pueden bajar el flujo de conocimiento humano y generar multiplicidad cuando la elasticidad excede cuatro. No sobrevive como afirmación general el **colapso total**: exige simultáneamente complementariedad extrema $\Delta_I=0$, ausencia de un flujo autónomo suficiente de conocimiento general y ausencia de especialistas o aprendizaje persistente. El enunciado más fuerte defendible es “la IA agéntica puede desplazar el sistema hacia un steady state de conocimiento bajo; llegar exactamente a cero es una propiedad de frontera del baseline”.

## 6. Versiones

La versión de febrero dice que el bienestar es no monótono y tiene un máximo interior (abstract, p. 1; §§4.3, pp. 25–27). Una revisión fechada 5 de mayo de 2026 circula públicamente. No se importan de ella ecuaciones ni páginas; cualquier diferencia debe cotejarse antes de actualizar este repositorio.
