# Manual Técnico: Las 4 Herramientas de Investigación y Scraping

Este documento contiene la documentación completa, arquitectura y comandos de uso de los 4 repositorios clonados en tu espacio de trabajo (`c:\DropS-Scalanze\tools\`) para la prospección de productos ganadores y espionaje de competencia en Quito y Ecuador.

---

## 1. Mapa de las Herramientas en el Espacio de Trabajo

```
c:\DropS-Scalanze\
├── market_intelligence_quito.py        <-- Motor orquestador y CLI para Quito
├── dashboard.html                      <-- Dashboard visual interactivo completo
├── MANUAL_HERRAMIENTAS_REPOSITORIOS.md <-- Este manual técnico
└── tools/
    ├── alicelabs-scraper/              <-- Repo 1: IA Deal Score y señales en vivo
    ├── social-media-research-skills/   <-- Repo 2: 13 Agent Skills (Outliers, Hooks, Comments)
    ├── instagram-account-scraper/      <-- Repo 3: Scraper Python de perfiles y reels
    └── web-scraper-dropshipping/       <-- Repo 4: Extractor de AliExpress, Amazon y eBay
```

---

## 2. Repo 1: `alicelabs-llc/Scraper`
* **Ruta local:** `tools/alicelabs-scraper/`
* **Tipo:** Motor de inteligencia de producto con IA (BYOK) + Vite/React + Node.js.
* **Propósito:** Evaluar y calificar la probabilidad de éxito de un producto antes de invertir en pauta publicitaria.

### Arquitectura Clave:
1. **Fórmula del Deal Score (0 a 100):**
   Ubicada en `services/scoring.ts`:
   $$\text{Deal Score} = (0.55 \times \text{Trend Momentum}) + (0.35 \times \text{Margen Parseado}) + (0.10 \times \text{Enlace Fuente Real})$$
2. **Señales de Mercado Gratuitas en Vivo (Sin API Key):**
   Ubicada en `services/dataSources.ts`:
   * Escanea Reddit público (`r/dropship`, `r/ecommerce`, `r/Entrepreneur`, `r/BusinessIdeas`).
   * Escanea Hacker News vía API pública de Algolia.
   * Genera el prompt enriquecido para que el modelo de IA no alucine y use datos de hoy.

### Cómo Usarlo:
```bash
cd tools/alicelabs-scraper
npm install
npm run dev
```
Abre en tu navegador `http://localhost:5173` para ingresar tus API keys (Gemini, Claude, OpenAI o Groq) y correr comparativas de hasta 3 productos en paralelo.

---

## 3. Repo 2: `ScrapeCreators/social-media-research-skills`
* **Ruta local:** `tools/social-media-research-skills/`
* **Tipo:** Kit de 13 habilidades especializadas para agentes de IA (formato `SKILL.md`).
* **Propósito:** Transformar datos sociales públicos en decisiones estratégicas de negocio.

### Las Habilidades Clave para Ecuador:

| Habilidad | Carpeta | Uso Táctico |
| :--- | :--- | :--- |
| **`outlier-post-finder`** | `skills/outlier-post-finder/` | Detecta Reels o TikToks que consiguieron 5x a 10x más reproducciones que el promedio de la cuenta. |
| **`transcript-intelligence`** | `skills/transcript-intelligence/` | Extrae los ganchos (*hooks*) de los primeros 3 segundos y las afirmaciones de venta de videos virales. |
| **`comment-mining`** | `skills/comment-mining/` | Extrae objeciones, preguntas frecuentes y lenguaje del cliente (Voice of Customer). |
| **`ad-library-teardown`** | `skills/ad-library-teardown/` | Analiza los anuncios activos en Meta Ads Library para identificar qué creativos llevan meses vendiendo. |
| **`product-demand-research`**| `skills/product-demand-research/` | Valida la demanda de un producto antes de importarlo o listarlo en la tienda. |

---

## 4. Repo 3: `data-scrape/instagram-account-scraper`
* **Ruta local:** `tools/instagram-account-scraper/`
* **Tipo:** Biblioteca y CLI de Python basada en `instaloader`.
* **Propósito:** Extraer datos públicos de perfiles, publicaciones, reels y métricas de competidores en Instagram.

### Dependencias Instaladas:
* `instaloader` (v4.15.4)
* `requests`
* `pandas`

### Comandos de Ejecución:
Puedes usar el CLI directamente desde `tools/instagram-account-scraper/src`:

```bash
# Ver información pública de un perfil (ej. importadora en Quito)
python -m ig_scraper.cli profile mecimportadora

# Extraer los últimos 10 posts y exportarlos a JSON
python -m ig_scraper.cli posts mecimportadora --limit 10 --output mec_posts.json

# Extraer los últimos reels para analizar visualizaciones
python -m ig_scraper.cli reels importadoramustafa --limit 10 --output mustafa_reels.json

# Usar una sesión para evitar bloqueos 429
python -m ig_scraper.cli --session tu_sesion.session profile mecimportadora
```

---

## 5. Repo 4: `ThiagoA20/web-scraper-for-dropshipping`
* **Ruta local:** `tools/web-scraper-dropshipping/`
* **Tipo:** Scripts en Python con Selenium y Pandas.
* **Propósito:** Extraer títulos, imágenes, precios en USD y especificaciones técnicas desde AliExpress, Amazon y eBay.

### Módulos Principales:
* `scrape_aliexpress.py`: Extrae precios y variantes de productos en AliExpress.
* `scrape_amazon.py`: Extrae listados de productos y valoraciones en Amazon.
* `scrape_ebay.py`: Extrae catálogos de eBay.
* `products_dataframe.py`: Consolida la información en un DataFrame estructurado para exportar a Excel/CSV.

---

## 6. Integración Unificada: `market_intelligence_quito.py`

En la raíz del proyecto unificamos la lógica de estos 4 repositorios adaptada al modelo de **Pago Contra Entrega (COD)** de Quito:

```bash
# 1. Ranking de tiendas con más seguidores y engagement en Ecuador
python market_intelligence_quito.py --ranking

# 2. Mapeo de mayoristas y debilidades explotables en Quito
python market_intelligence_quito.py --competitors

# 3. Ganchos virales para Skincare y Mascotas
python market_intelligence_quito.py --hooks

# 4. Los 4 guiones de Neuromarketing para el nicho "Perrhijos" en Quito
python market_intelligence_quito.py --perrhijos

# 5. Simulador financiero con fletes y devoluciones reales de Ecuador
python market_intelligence_quito.py --finance --cost 4.20 --pvp 21.99 --cpa 5.00
```
