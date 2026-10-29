"""
Panas Bikers - Market Intelligence & E-Commerce Dropshipping CLI (Quito, Ecuador)
Herramienta de análisis de mercado, ranking competitivo, finanzas unitarias COD y ganchos virales
diseñada específicamente para el nicho motero de Panas Bikers y Scalanze.
"""

import sys
import os
import argparse
from datetime import datetime

# Configurar encoding UTF-8 para salida en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

TOP_BIKER_STORES = [
    {
        "rank": 1,
        "name": "Tienda Motera EC",
        "username": "tiendamoteraec",
        "followers": "~55,000",
        "focus": "Cascos gama media/alta y chaquetas",
        "engagement": "Medio (~1.4%)",
        "debilidad": "Modelo tradicional de tienda física; no entregan el mismo día con motorizado ni ofrecen prueba de tallas a domicilio."
    },
    {
        "rank": 2,
        "name": "Motos Quito",
        "username": "motosquito",
        "followers": "~35,000",
        "focus": "Accesorios visuales, sliders y exploradoras",
        "engagement": "Alto en Reels (~3.8%)",
        "debilidad": "Cero automatización e-commerce; dicen 'Precio al DM' y demoran más de 6 horas en responder WhatsApp."
    },
    {
        "rank": 3,
        "name": "ProCircuit Ecuador",
        "username": "procircuit_ec",
        "followers": "~40,000",
        "focus": "Equipamiento touring y enduro de alta gama (KTM/BMW)",
        "engagement": "Medio (~1.5%)",
        "debilidad": "Precios prohibitivos; desatienden al segmento urbano y repartidores de 125-250cc (Pulsar, Suzuki, Shineray)."
    },
    {
        "rank": 4,
        "name": "Motostok Ecuador",
        "username": "motostok_ecuador",
        "followers": "~45,000",
        "focus": "Repuestos de motor y accesorios generales",
        "engagement": "Bajo (~0.9%)",
        "debilidad": "Catálogo estático sin videos demostrativos ni pruebas de tortura de producto."
    },
    {
        "rank": 5,
        "name": "Importadora Motos UIO",
        "username": "importadoramotos_uio",
        "followers": "~20,000",
        "focus": "Venta al por mayor en bodega (La Marín)",
        "engagement": "Bajo (~0.7%)",
        "debilidad": "Cero experiencia B2C, sin garantía al consumidor final ni cobro con Deuna/Transferencia en puerta."
    }
]

PRODUCTS_CATALOG = {
    "candado": {
        "name": "Candado de Disco con Alarma 110dB",
        "costo": 6.20,
        "pvp": 22.00,
        "flete": 2.80,
        "cpa": 3.50,
        "deal_score": 96,
        "dolor": "Robo de motos en veredas en Quito (jaloneo en 30s)."
    },
    "exploradoras": {
        "name": "Exploradoras Búho Dual Ámbar/Blanco",
        "costo": 12.50,
        "pvp": 35.00,
        "flete": 3.00,
        "cpa": 5.00,
        "deal_score": 94,
        "dolor": "Ceguera en niebla andina (Papallacta/Alóag) y multas ANT."
    },
    "soporte": {
        "name": "Soporte Celular Aluminio CNC Antivibración",
        "costo": 8.00,
        "pvp": 24.00,
        "flete": 2.80,
        "cpa": 3.50,
        "deal_score": 92,
        "dolor": "Destrucción del estabilizador óptico OIS de iPhone/Samsung."
    },
    "botas": {
        "name": "Botas SPEED Racing Antitorsión",
        "costo": 26.00,
        "pvp": 74.00,
        "flete": 3.50,
        "cpa": 7.00,
        "deal_score": 95,
        "dolor": "65% de fracturas en moto son de tobillo/pie por calzado casual."
    },
    "alarma": {
        "name": "Alarma 125dB con 2 Controles",
        "costo": 7.50,
        "pvp": 26.00,
        "flete": 2.80,
        "cpa": 4.00,
        "deal_score": 90,
        "dolor": "Falta de corte de encendido y aviso sonoro a distancia."
    },
    "guantes": {
        "name": "Guantes Pro-Biker Táctiles Nudillos Carbono",
        "costo": 4.50,
        "pvp": 16.00,
        "flete": 2.50,
        "cpa": 2.50,
        "deal_score": 89,
        "dolor": "Abrasión palmar en caída y agarre resbaloso bajo lluvia."
    },
    "impermeable": {
        "name": "Impermeable 2 Piezas Reforzado Termosellado",
        "costo": 9.50,
        "pvp": 28.00,
        "flete": 3.00,
        "cpa": 3.50,
        "deal_score": 91,
        "dolor": "Empaparse en tormentas andinas de Quito a 10°C."
    },
    "aceite": {
        "name": "Aceite Motul 7100 4T 10W-40 100% Sintético",
        "costo": 13.80,
        "pvp": 20.50,
        "flete": 2.50,
        "cpa": 1.50,
        "deal_score": 93,
        "dolor": "Degradación térmica por ralentí en trancones (El Trébol/Mariscal)."
    }
}

def print_banner():
    print("=" * 70)
    print("   PANAS BIKERS - MARKET INTELLIGENCE & COD ANALYZER (QUITO)   ")
    print("        Infraestructura E-Commerce & Growth Scalanze 2026       ")
    print("=" * 70)

def display_stores():
    print("\n[+] RADAR DE TIENDAS Y MAYORISTAS BIKER EN QUITO & ECUADOR:")
    print("-" * 70)
    for s in TOP_BIKER_STORES:
        print(f"#{s['rank']} {s['name']} (@{s['username']}) - Audiencia: {s['followers']}")
        print(f"   Enfoque:     {s['focus']} | Engagement: {s['engagement']}")
        print(f"   Brecha Oportunidad: {s['debilidad']}")
        print("-" * 70)

def display_catalog():
    print("\n[+] CATÁLOGO GANADOR PANAS BIKERS (SCORING IA & ECONOMÍA UNITARIA):")
    print("-" * 70)
    print(f"{'PRODUCTO':<32} {'COSTO':<8} {'PVP':<8} {'NETO':<10} {'% NETO':<8} {'DEAL SCORE'}")
    print("-" * 70)
    for k, p in PRODUCTS_CATALOG.items():
        costo_total = p['costo'] + p['flete'] + p['cpa']
        neto = p['pvp'] - costo_total
        pct = (neto / p['pvp']) * 100
        print(f"{p['name'][:30]:<32} ${p['costo']:<7.2f} ${p['pvp']:<7.2f} +${neto:<8.2f} {pct:>5.1f}%   {p['deal_score']}/100")
    print("-" * 70)

def simulate_finance(cost, pvp, flete, cpa, return_rate=0.075):
    bruto = pvp - cost
    costo_operativo = cost + flete + cpa
    loss_return = flete * return_rate
    neto = pvp - (costo_operativo + loss_return)
    pct = (neto / pvp) * 100 if pvp > 0 else 0
    break_even_roas = pvp / (pvp - (cost + flete)) if (pvp - (cost + flete)) > 0 else 1.8

    print("\n" + "=" * 55)
    print("   SIMULACIÓN FINANCIERA UNITARIA BIKER (QUITO COD)   ")
    print("=" * 55)
    print(f"  Precio de Venta al Público (PVP):      ${pvp:>7.2f} USD")
    print(f"  Costo Base del Producto:               ${cost:>7.2f} USD")
    print(f"  Flete Motorizado Local (Quito DMQ):    ${flete:>7.2f} USD")
    print(f"  Costo Adquisición Cliente (CPA Ads):   ${cpa:>7.2f} USD")
    print(f"  Tasa Estimada Rechazo en Puerta:       {return_rate*100:>7.1f}%")
    print("-" * 55)
    print(f"  Margen Bruto (PVP - Costo):            ${bruto:>7.2f} USD")
    print(f"  Pérdida por Devolución Ponderada:      ${loss_return:>7.2f} USD")
    print(f"  ROAS de Equilibrio (Break-Even):       {break_even_roas:>7.2f}x")
    print("-" * 55)
    color_pref = "+" if neto >= 0 else ""
    print(f"  GANANCIA NETA LIMPIA POR UNIDAD:     {color_pref}${neto:>7.2f} USD ({pct:.1f}%)")
    print("=" * 55)

def display_hooks():
    print("\n[+] HOOKS VIRALES DE 3 SEGUNDOS PARA REELS BIKER (OUTLIERS):")
    print("-" * 70)
    print("1. [ANTIRROBO]: 'Así se jalaron una Pulsar en la Villa Flora en 20 segundos 💔'")
    print("   -> Sonido real de alarma 110dB + amoladora + demostración de corte de ignición.")
    print("\n2. [NIEBLA ANDINA]: 'Por qué la luz blanca LED es tu peor enemiga en Papallacta 🌧️'")
    print("   -> Comparación en cámara térmica/niebla: haz blanco encandila vs haz ámbar 3000K penetra.")
    print("\n3. [OIS CELULAR]: 'Tu moto monocilíndrica está rompiendo el lente de tu iPhone 📱💥'")
    print("   -> Martillazo a soporte de plástico barato (roto) vs aluminio CNC Panas Bikers (intacto).")
    print("\n4. [BOTAS VS ZAPATILLAS]: 'A 40 km/h, una zapatilla de lona dura 0.3 segundos en el asfalto 🦶'")
    print("   -> Protección antitorsión de maléolo + motorizado lleva 2 tallas para prueba en casa.")
    print("-" * 70)

def main():
    parser = argparse.ArgumentParser(description="Panas Bikers Intelligence CLI")
    parser.add_argument("--stores", action="store_true", help="Mostrar radar de tiendas moteras en Quito")
    parser.add_argument("--catalog", action="store_true", help="Listar catálogo ganador y Deal Scores")
    parser.add_argument("--hooks", action="store_true", help="Mostrar swipe file de hooks virales")
    parser.add_argument("--finance", action="store_true", help="Ejecutar simulación financiera")
    parser.add_argument("--cost", type=float, default=8.00, help="Costo base del producto")
    parser.add_argument("--pvp", type=float, default=24.00, help="PVP en Quito")
    parser.add_argument("--flete", type=float, default=2.80, help="Flete motorizado")
    parser.add_argument("--cpa", type=float, default=3.50, help="Costo CPA")
    parser.add_argument("--product", type=str, help="Calcular finanzas de un producto específico (candado, exploradoras, soporte, botas, etc.)")

    args = parser.parse_args()

    print_banner()

    if args.product:
        prod_key = args.product.lower()
        if prod_key in PRODUCTS_CATALOG:
            p = PRODUCTS_CATALOG[prod_key]
            print(f"\n[+] Análisis de Producto: {p['name']}")
            print(f"    Dolor que resuelve: {p['dolor']}")
            simulate_finance(p['costo'], p['pvp'], p['flete'], p['cpa'])
        else:
            print(f"\n[!] Producto '{args.product}' no encontrado. Opciones: {list(PRODUCTS_CATALOG.keys())}")
        return

    if args.finance:
        simulate_finance(args.cost, args.pvp, args.flete, args.cpa)
        return

    if args.stores:
        display_stores()
        return

    if args.catalog:
        display_catalog()
        return

    if args.hooks:
        display_hooks()
        return

    # Default: Show summary
    display_catalog()
    display_stores()
    display_hooks()

if __name__ == "__main__":
    main()
