# DropS-Scalanze: Sistema de Inteligencia y Dropshipping en Quito

Sistema integrado para investigación de mercado, análisis de competidores mayoristas en Quito y cálculo de viabilidad de productos bajo el modelo de Pago Contra Entrega (COD) en Ecuador.

## Documentación y Manuales Disponibles (.md)

* 📘 **[MANUAL_HERRAMIENTAS_REPOSITORIOS.md](file:///c:/DropS-Scalanze/MANUAL_HERRAMIENTAS_REPOSITORIOS.md)**: Manual técnico completo de los 4 repositorios clonados en `tools/`, su arquitectura, dependencias y comandos de ejecución.
* 🌐 **[dashboard.html](file:///c:/DropS-Scalanze/dashboard.html)**: Dashboard interactivo completo con comparativa de nichos, psicología de perrhijos, swipe file de enlaces y simulador financiero COD.
* 🐍 **[market_intelligence_quito.py](file:///c:/DropS-Scalanze/market_intelligence_quito.py)**: CLI central para simulación financiera y auditoría de competidores.

## Repositorios Clonados en `tools/`

1. `tools/alicelabs-scraper`: Algoritmos de Deal Score (v5.1) y señales de mercado en vivo de Reddit y Google Trends.
2. `tools/social-media-research-skills`: 13 habilidades de IA para análisis social (Outliers, Hooks, Comment Mining).
3. `tools/instagram-account-scraper`: Motor Python con `instaloader` para extracción de perfiles y reels.
4. `tools/web-scraper-dropshipping`: Scrapers para AliExpress, Amazon y eBay.

## Comandos Rápidos del CLI

```bash
# Ver los 4 guiones de neuromarketing para el nicho "Perrhijos" en Quito
python market_intelligence_quito.py --perrhijos

# Ranking de tiendas con más seguidores y engagement
python market_intelligence_quito.py --ranking

# Mapeo de mayoristas y distribuidores en Quito
python market_intelligence_quito.py --competitors

# Simulación financiera personalizada
python market_intelligence_quito.py --finance --cost 4.20 --pvp 21.99 --cpa 5.00
```

