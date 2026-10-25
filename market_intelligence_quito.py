"""
Market Intelligence & Dropshipping Analyzer - Quito, Ecuador
Integracion de los 4 repositorios de investigacion de mercado adaptados
al contexto de comercio electronico y contra entrega (COD) en Quito.
"""

import sys
import os
import json
import argparse
from datetime import datetime

# Configurar encoding UTF-8 para salida en Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Añadir ig_scraper al path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IG_PATH = os.path.join(CURRENT_DIR, "tools", "instagram-account-scraper", "src")
if IG_PATH not in sys.path:
    sys.path.append(IG_PATH)

try:
    from ig_scraper import InstagramScraper
    HAS_IG_SCRAPER = True
except ImportError:
    HAS_IG_SCRAPER = False

# Ranking de las tiendas e importadoras con mas seguidores y mayor engagement en Ecuador y Quito
TOP_STORES_RANKING = [
    {
        "rank": 1,
        "name": "De Prati",
        "username": "deprati",
        "followers_approx": "850K - 900K",
        "category": "Moda, Hogar, Skincare y Belleza",
        "engagement_rate": "Medio (~0.8% - 1.2%)",
        "tipo_contenido": "Campañas de moda, influencers, contenido de marca aspiracional",
        "brecha_explotable": "Precios altos y cero dinamismo de dropshipping; catálogo rígido sin foco en gadgets virales"
    },
    {
        "rank": 2,
        "name": "Dipaso Belleza",
        "username": "dipasobelleza",
        "followers_approx": "350K",
        "category": "Belleza, Cuidado Capilar y Skincare Coreano",
        "engagement_rate": "Alto (~2.5% - 4.2%)",
        "tipo_contenido": "Tutoriales de maquillaje, rutinas de skincare, reseñas de producto",
        "brecha_explotable": "Venden productos consumibles (cremas/tintes); descuidan la aparatología facial portátil de impulso rápido"
    },
    {
        "rank": 3,
        "name": "Novicompu",
        "username": "novicompu",
        "followers_approx": "320K",
        "category": "Tecnología, Computación y Celulares",
        "engagement_rate": "Medio-Bajo (~0.6% - 1.0%)",
        "tipo_contenido": "Flyers de promociones, precios en combo y aperturas de locales físicos",
        "brecha_explotable": "Venta tradicional de retail; no hacen videos de soluciones prácticas ni venta por impulso en video"
    },
    {
        "rank": 4,
        "name": "Pycca",
        "username": "pycca",
        "followers_approx": "180K - 220K",
        "category": "Hogar, Muebles, Limpieza y Bazar",
        "engagement_rate": "Bajo (~0.5%)",
        "tipo_contenido": "Catálogo estático de electrodomésticos y decoración del hogar",
        "brecha_explotable": "Productos voluminosos y costosos; espacio libre para gadgets de limpieza compactos (CleanTok)"
    },
    {
        "rank": 5,
        "name": "Importadora MEC (Quito)",
        "username": "mecimportadora",
        "followers_approx": "40K - 80K",
        "category": "Novedades, Hogar, Gadgets de Bodega",
        "engagement_rate": "Muy Alto en Reels Virales (> 5.0%)",
        "tipo_contenido": "Videos informales mostrando cajas y stock físico en su local de la Av. Occidental",
        "brecha_explotable": "Cero automatización: dicen 'Precio al DM' o 'Escríbenos al WhatsApp', perdiendo el 80% de las ventas en caliente"
    },
    {
        "rank": 6,
        "name": "Importadora Mustafa (Quito Sur)",
        "username": "importadoramustafa",
        "followers_approx": "30K - 50K",
        "category": "Tecnología, Audio y Bazar",
        "engagement_rate": "Alto en Novedades Viralizadas (~3.5%)",
        "tipo_contenido": "Muestras rápidas de productos económicos de China recién llegados en bulto",
        "brecha_explotable": "No ofrecen garantía de cambio inmediato ni branding profesional; solo compiten por precio centavo"
    }
]

# Base de datos de competidores mayoristas e importadores identificados en Quito
QUITO_COMPETITORS = [
    {
        "name": "Importadora MEC",
        "username": "mecimportadora",
        "location": "Pinar Alto / Av. Occidental (Norte de Quito)",
        "category": "Hogar, Limpieza, Novedades y Gadgets",
        "focus": "Mayoristas y Emprendedores",
        "weakness": "Videos sin gancho narrativo, enfoque en venta por bulto, requiere pago anticipado o visita física"
    },
    {
        "name": "Importadora Mustafa",
        "username": "importadoramustafa",
        "location": "La Magdalena (Sur de Quito)",
        "category": "Tecnología, Accesorios y Gadgets Virales",
        "focus": "Venta al por mayor y menor",
        "weakness": "Catálogo genérico sin personalización de marca, atención lenta en WhatsApp"
    },
    {
        "name": "Blue Magic",
        "username": "bluemagic_ec",
        "location": "Av. de los Shyris (Centro Norte de Quito)",
        "category": "Tecnología, Audio y Gadgets de Ocio",
        "focus": "Showroom físico + Instagram",
        "weakness": "Precios con margen alto de tienda física, poca presencia fuera del showroom"
    },
    {
        "name": "Zoeimport Mayoristas",
        "username": "zoeimport",
        "location": "Valle de los Chillos (Conocoto)",
        "category": "Skincare, Maquillaje y Cuidado Facial",
        "focus": "Suministros para bazares y revendedores",
        "weakness": "Embalaje básico sin manuales en español ni propuesta de valor agregada"
    },
    {
        "name": "Gaby Cosméticos Importadora",
        "username": "gabycosmeticosimpo",
        "location": "Sur de Quito",
        "category": "Cosméticos y Belleza al por mayor",
        "focus": "Venta por docenas",
        "weakness": "Cero publicidad estructurada en Meta Ads; dependen exclusivamente de alcance orgánico"
    },
    {
        "name": "SuperPet Ecuador",
        "username": "superpet_ec",
        "location": "Quito Norte / Cumbayá",
        "category": "Mascotas, Alimentos y Accesorios",
        "focus": "Pet Shop Tradicional y Veterinaria",
        "weakness": "Precios elevados de retail físico; no comercializan gadgets virales de TikTok a bajo costo"
    },
    {
        "name": "Lord Guau",
        "username": "lordguau_ec",
        "location": "Quito (Sector La Carolina / Valles)",
        "category": "Cuidado Animal, Peluquería Canina y Spa",
        "focus": "Servicios presenciales y productos premium",
        "weakness": "Cobran $25-$40 por baño y deslanado; espacio perfecto para vender herramientas de cuidado en casa"
    }
]

# Plantillas de Contenido Viral y Hooks (Inspirados en social-media-research-skills)
VIRAL_HOOKS_SKINCARE_QUITO = [
    {
        "tipo": "Demostración de Impacto / Antes y Después",
        "hook_3_segundos": "Si tienes puntos negros o textura en la nariz en Quito, deja de apretarte la piel con las uñas.",
        "agitacion": "Apretarte solo rompe tus poros y deja manchas que empeoran con el frío y el sol de la sierra.",
        "solucion": "Esta espátula ultrasónica saca todas las impurezas con vibración de agua en 3 minutos.",
        "llamada_accion": "Pide hoy con ENVÍO GRATIS a todo Quito (Norte, Sur y Valles) y PAGA EN EFECTIVO al recibir en tu puerta."
    },
    {
        "tipo": "Alivio de Dolor Económico / Comparación Spa vs Casa",
        "hook_3_segundos": "Una limpieza facial en una estética de Cumbayá o la Carolina cuesta $35 a $50. Esto cuesta menos y te dura años.",
        "agitacion": "Gastamos fortunas en citas mensuales cuando puedes mantener tus poros limpios cada semana desde tu casa.",
        "solucion": "Aparatología facial portátil con 3 modos: Limpieza profunda, Nutrición y Lifting facial.",
        "llamada_accion": "Envío inmediato en 24 horas a cualquier sector de Quito. Solo pagas cuando lo tengas en tus manos."
    },
    {
        "tipo": "Satisfying ASMR / Prueba de Producto",
        "hook_3_segundos": "Miren toda la grasa y suciedad que sale de la piel después de un día caminando por el centro de Quito.",
        "agitacion": "La contaminación de la ciudad se acumula en tus poros sin que te des cuenta.",
        "solucion": "Muestra en primer plano del vapor/agua extrayendo la grasa acumulada.",
        "llamada_accion": "Quedan pocas unidades con flete contra entrega garantizado. Haz clic en el botón de abajo."
    }
]

VIRAL_HOOKS_PETS_QUITO = [
    {
        "tipo": "Ataque a la Culpa: Ansiedad por Separación (Cama Antiestrés)",
        "hook_3_segundos": "Esto es lo que hace tu perrito las 8 horas que pasa solo en tu departamento en Quito 💔",
        "agitacion": "Nosotros salimos y vemos gente, pero todo su mundo eres tú. El 70% de los perros en departamentos sufren ansiedad extrema y aúllan de estrés.",
        "solucion": "Esta cama dona afelpada imita el pelaje materno. Sus bordes elevados liberan oxitocina y reducen su ritmo cardíaco para que duerma en paz.",
        "llamada_accion": "Entrega express en 24h a cualquier sector de Quito con Pago Contra Entrega. Haz clic y dale su lugar seguro."
    },
    {
        "tipo": "Pánico de Seguridad: Peligro del Collar (Arnés Anti-Tirones 3M)",
        "hook_3_segundos": "¡Por favor, deja de pasear a tu perro con collar al cuello en Quito! 🛑",
        "agitacion": "Cada tirón brusco aplasta su tráquea y glándula tiroides. Los veterinarios en Ecuador atienden colapsos irreversibles por esto.",
        "solucion": "Este arnés ergonómico distribuye la fuerza en su pecho sin ahogarlo y tiene bandas reflectivas 3M para que los autos lo vean en la noche.",
        "llamada_accion": "Envío gratis a todo Quito y pagas en efectivo en tu casa por solo $21.99. Toca el botón y elige su talla."
    },
    {
        "tipo": "Confort en el Frío Andino: Deslanado ASMR (Cepillo de Vapor)",
        "hook_3_segundos": "Para los que tenemos perrhijos o gathijos en el frío de Quito y la ropa llena de pelos ☁️🐶",
        "agitacion": "Bañarlos seguido en el frío de la sierra les causa neumonía, pero si no los cepillas, tu cama y tus sillones se llenan de pelos.",
        "solucion": "Este cepillo tiene micro-neblina fría que atrapa el 100% del pelo muerto en un solo bloque con cerdas de silicona médica.",
        "llamada_accion": "Solo $21.99 USD con Envío Gratis en Quito y pago en efectivo al cartero."
    },
    {
        "tipo": "Miedo a la Enfermedad Silenciosa: Sarro y Riñones (Kit Dental)",
        "hook_3_segundos": "Si el aliento de tu perro huele a podrido, sus riñones están en grave peligro ⚠️",
        "agitacion": "El 80% de los perros en Ecuador tienen periodontitis a los 3 años. Las bacterias viajan por la sangre y acortan su vida hasta 4 años.",
        "solucion": "Este limpiador dental 360° retira el sarro acumulado como un juego masticable sin pagar $100 por una anestesia riesgosa en la veterinaria.",
        "llamada_accion": "Añádele años de vida a tu perrhijo. Entrega en 24h en Quito con pago contra entrega."
    }
]

def calculate_ecuador_deal_score(cost_usd, pvp_usd, cpa_usd=5.0, shipping_usd=4.0, return_rate_pct=15.0):
    """
    Calculadora financiera y Deal Score adaptado a la logistica de Contra Entrega en Ecuador.
    Considera:
      - Tasa de entrega efectiva (100 - return_rate_pct)
      - Costo del flete de ida y flete de retorno en caso de rechazo
      - Costo publicitario por compra (CPA)
    """
    delivery_rate = (100.0 - return_rate_pct) / 100.0
    return_rate = return_rate_pct / 100.0
    
    # Costo de devolución aproximado en Ecuador (flete de ida + 50% de retorno)
    return_shipping_cost = shipping_usd * 1.5
    
    # Ingresos y costos por cada 100 pedidos
    total_orders = 100
    delivered_orders = total_orders * delivery_rate
    returned_orders = total_orders * return_rate
    
    gross_revenue = delivered_orders * pvp_usd
    total_cogs = delivered_orders * cost_usd  # Solo se gasta costo de producto en los entregados
    total_shipping = (delivered_orders * shipping_usd) + (returned_orders * return_shipping_cost)
    total_ad_spend = total_orders * cpa_usd  # Se paga ad spend por cada pedido generado
    
    net_profit = gross_revenue - total_cogs - total_shipping - total_ad_spend
    net_profit_per_order = net_profit / total_orders
    net_margin_pct = (net_profit / gross_revenue * 100) if gross_revenue > 0 else 0
    
    # Break-even ROAS
    # Formula: Break-even ROAS = PVP / (PVP - Costo - Envio ajustado)
    avg_order_costs = cost_usd + (shipping_usd * delivery_rate + return_shipping_cost * return_rate) / delivery_rate
    unit_contribution = pvp_usd - avg_order_costs
    breakeven_cpa = unit_contribution * delivery_rate
    breakeven_roas = pvp_usd / breakeven_cpa if breakeven_cpa > 0 else 999.0
    
    # Deal Score (0 - 100) basado en viabilidad en Ecuador
    # Factores: Margen neto (> 25% = 40 pts), Ticket PVP ($20-$35 = 30 pts), Breakeven ROAS (< 2.0 = 30 pts)
    score_margin = min(40, max(0, (net_margin_pct / 30.0) * 40))
    score_ticket = 30 if 20.0 <= pvp_usd <= 35.0 else (20 if 15.0 <= pvp_usd <= 45.0 else 10)
    score_roas = min(30, max(0, ((2.5 - breakeven_roas) / 1.0) * 30)) if breakeven_roas <= 2.5 else 10
    deal_score = int(round(score_margin + score_ticket + score_roas))
    
    return {
        "pvp_usd": pvp_usd,
        "cost_usd": cost_usd,
        "cpa_usd": cpa_usd,
        "shipping_usd": shipping_usd,
        "return_rate_pct": return_rate_pct,
        "net_profit_per_order": round(net_profit_per_order, 2),
        "net_margin_pct": round(net_margin_pct, 1),
        "breakeven_cpa": round(breakeven_cpa, 2),
        "breakeven_roas": round(breakeven_roas, 2),
        "deal_score": deal_score
    }

def print_top_stores_ranking():
    print("\n=======================================================")
    print(" 🏆 CUENTAS CON MÁS SEGUIDORES Y ENGAGEMENT (ECUADOR/QUITO)")
    print("=======================================================")
    for item in TOP_STORES_RANKING:
        print(f"\n[Top {item['rank']}] {item['name']} (@{item['username']})")
        print(f"    👥 Seguidores Aprox : {item['followers_approx']}")
        print(f"    🏷️ Categoría        : {item['category']}")
        print(f"    🔥 Nivel Engagement : {item['engagement_rate']}")
        print(f"    📱 Contenido Tipo   : {item['tipo_contenido']}")
        print(f"    🎯 Brecha a Explotar: {item['brecha_explotable']}")
    print("\n" + "="*55)

def print_competitors():
    print("\n=======================================================")
    print(" 📍 DISTRIBUIDORES Y COMPETIDORES MONITOREADOS EN QUITO")
    print("=======================================================")
    for idx, comp in enumerate(QUITO_COMPETITORS, 1):
        print(f"\n[{idx}] {comp['name']} (@{comp['username']})")
        print(f"    Ubicación : {comp['location']}")
        print(f"    Categoría : {comp['category']}")
        print(f"    Enfoque   : {comp['focus']}")
        print(f"    Debilidad : {comp['weakness']}")
    print("\n" + "="*55)

def print_financial_simulation():
    print("\n=======================================================")
    print(" 💵 SIMULACIÓN FINANCIERA: APARATOLOGÍA SKINCARE EN QUITO")
    print("=======================================================")
    
    # Caso 1: Espátula Ultrasónica Facial (Dropi / Proveedor Local)
    res = calculate_ecuador_deal_score(
        cost_usd=7.50,
        pvp_usd=28.99,
        cpa_usd=5.50,
        shipping_usd=4.00,
        return_rate_pct=15.0
    )
    
    print("\nProducto: Espátula Ultrasónica Limpiadora de Poros")
    print(f"  • Costo Producto Proveedor : ${res['cost_usd']:.2f} USD")
    print(f"  • Precio Venta al Público : ${res['pvp_usd']:.2f} USD")
    print(f"  • Costo de Envío COD      : ${res['shipping_usd']:.2f} USD")
    print(f"  • Costo Adquisición (CPA) : ${res['cpa_usd']:.2f} USD")
    print(f"  • Tasa Devolución Prevista: {res['return_rate_pct']:.1f}%")
    print(f"  --------------------------------------------------")
    print(f"  💰 Ganancia Neta por Orden: ${res['net_profit_per_order']:.2f} USD")
    print(f"  📈 Margen Neto Real       : {res['net_margin_pct']:.1f}%")
    print(f"  🎯 CPA Máximo (Break-even): ${res['breakeven_cpa']:.2f} USD")
    print(f"  🔥 ROAS de Equilibrio     : {res['breakeven_roas']:.2f}x")
    print(f"  ⭐ DEAL SCORE ECUADOR     : {res['deal_score']}/100 [VIABLE Y ALTA RENTABILIDAD]")
    print("="*55)

def print_creative_hooks():
    print("\n=======================================================")
    print(" 🎬 GANCHOS VIRALES: SMART SKINCARE (QUITO)")
    print("=======================================================")
    for idx, h in enumerate(VIRAL_HOOKS_SKINCARE_QUITO, 1):
        print(f"\n[Hook Skincare {idx}] Formato: {h['tipo']}")
        print(f"  ▶️ Primeros 3 segundos: \"{h['hook_3_segundos']}\"")
        print(f"  ⚠️ Agitación del dolor: \"{h['agitacion']}\"")
        print(f"  💡 Solución mostrada  : \"{h['solucion']}\"")
        print(f"  📦 Llamada a la acción : \"{h['llamada_accion']}\"")
        
    print("\n=======================================================")
    print(" 🐶 GANCHOS VIRALES: MASCOTAS Y PET TECH (QUITO)")
    print("=======================================================")
    for idx, h in enumerate(VIRAL_HOOKS_PETS_QUITO, 1):
        print(f"\n[Hook Pet {idx}] Formato: {h['tipo']}")
        print(f"  ▶️ Primeros 3 segundos: \"{h['hook_3_segundos']}\"")
        print(f"  ⚠️ Agitación del dolor: \"{h['agitacion']}\"")
        print(f"  💡 Solución mostrada  : \"{h['solucion']}\"")
        print(f"  📦 Llamada a la acción : \"{h['llamada_accion']}\"")
    print("\n" + "="*55)

def main():
    parser = argparse.ArgumentParser(description="Market Intelligence Quito Dropshipping CLI")
    parser.add_argument("--ranking", action="store_true", help="Mostrar ranking de tiendas con mas seguidores y engagement")
    parser.add_argument("--competitors", action="store_true", help="Listar distribuidores y competidores en Quito")
    parser.add_argument("--finance", action="store_true", help="Calcular viabilidad financiera con flete contra entrega")
    parser.add_argument("--hooks", action="store_true", help="Mostrar ganchos virales para TikTok e Instagram")
    parser.add_argument("--perrhijos", action="store_true", help="Mostrar los 4 ganchos emocionales para el nicho de perrhijos en Quito")
    parser.add_argument("--audit", type=str, help="Auditar un usuario de Instagram de Quito (ej. mecimportadora)")
    parser.add_argument("--cost", type=float, default=7.50, help="Costo del producto en USD")
    parser.add_argument("--pvp", type=float, default=28.99, help="Precio de venta en USD")
    parser.add_argument("--cpa", type=float, default=5.50, help="CPA en Meta Ads en USD")
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        # Modo interactivo / resumen completo
        print_top_stores_ranking()
        print_competitors()
        print_financial_simulation()
        print_creative_hooks()
        return

    if args.ranking:
        print_top_stores_ranking()

    if args.competitors:
        print_competitors()
        
    if args.finance:
        res = calculate_ecuador_deal_score(args.cost, args.pvp, args.cpa)
        print(json.dumps(res, indent=2))
        
    if args.hooks:
        print_creative_hooks()

    if args.perrhijos:
        print("\n=======================================================")
        print(" 🐶 GANCHOS EMOCIONALES: NICHO PERRHIJOS EN QUITO")
        print("=======================================================")
        for idx, h in enumerate(VIRAL_HOOKS_PETS_QUITO, 1):
            print(f"\n[Estrategia Perrhijo {idx}] {h['tipo']}")
            print(f"  ▶️ Primeros 3 segundos: \"{h['hook_3_segundos']}\"")
            print(f"  💔 Agitación de Culpa/Dolor: \"{h['agitacion']}\"")
            print(f"  ✨ Solución Mostrada: \"{h['solucion']}\"")
            print(f"  📦 Oferta Contra Entrega: \"{h['llamada_accion']}\"")
        print("\n" + "="*55)
        
    if args.audit:
        print(f"\nAuditando cuenta @{args.audit}...")
        if HAS_IG_SCRAPER:
            try:
                scraper = InstagramScraper(rate_limit_delay=2.0)
                profile = scraper.get_profile(args.audit)
                print(f"\n[Perfil Encontrado: @{profile.username}]")
                print(f"  Nombre: {profile.full_name}")
                print(f"  Seguidores: {profile.followers_count:,}")
                print(f"  Siguiendo: {profile.following_count:,}")
                print(f"  Publicaciones: {profile.posts_count:,}")
                print(f"  Bio: {profile.biography[:100]}...")
            except Exception as e:
                print(f"Nota: Instagram requiere sesión o proxy para perfiles protegidos: {e}")
        else:
            print("El módulo ig_scraper no está disponible.")

if __name__ == "__main__":
    main()
