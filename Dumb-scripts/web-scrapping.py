#!/usr/bin/env python3


#PARSEANDO HTML

#Importo el modulo de beautiful soup 4
import bs4, requests

#DESCARGO EL HTML de el link que paso
response = requests.get('https://articulo.mercadolibre.com.ar/MLA-746729363-monitor-tv-led-24-pulgadas-hd-audio-rca-hdmi-vga-lcd-usb-electroshows-_JM?variation=37119602551&quantity=1#reco_item_pos=2&reco_backend=promotions-sorted-by-score-mla-B&reco_backend_type=low_level&reco_client=home_seller-promotions-recommendations&reco_id=3d091023-3b39-49b7-b6f7-1e98c10492d3&c_id=/home/promotions-recommendations/element&c_element_order=3&c_uid=69382155-6856-42ed-959b-eca725a177b')

#Verifico que no haya habido ningun error en la descarga, en caso de que el metodo devuelve Exceppcion
response.raise_for_status()

#Creo un objeto bs4, el segundo parametro es para evitar warnings
soup = bs4.BeautifulSoup(response.text, 'html.parser')

#Con F12 source de la pagina puedo ubicar el dato que quiero traer con la opcion de CCS Selector o CSS Path
#Se guarda como lista en elem
elem = soup.select('fieldset.item-price > span:nth-child(2) > span:nth-child(2)')

#Como solo tiene un elemento la lista me quedo con esa [0] y lo paso a texto\
#Es importante recorddar que podemos usar strip() para quitar los saltos de linea
print(elem[0].text)

