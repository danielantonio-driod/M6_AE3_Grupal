from recetas_app.models import Receta

Receta.objects.create(
    nombre="Spaghetti Carbonara",
    ingredientes="""
- 400g de spaghetti
- 200g de panceta o bacon
- 2 huevos
- 50g de queso parmesano rallado
- Sal y pimienta negra al gusto
""",
    instrucciones="""
1. Cocina los spaghetti en abundante agua con sal hasta que estén al dente.
2. Mientras tanto, corta la panceta en tiras y fríela en una sartén hasta que esté dorada.
3. En un bol, bate los huevos y mézclalos con el queso parmesano rallado, sal y pimienta.
4. Escurre la pasta y mézclala rápidamente con la panceta caliente.
5. Retira del fuego y añade la mezcla de huevo y queso, removiendo bien para que el calor de la pasta cocine ligeramente el huevo.
6. Sirve inmediatamente con más queso y pimienta al gusto.
""",
    imagen="carbonara.jpg"
)

Receta.objects.create(
    nombre="Risotto de Champiñones",
    ingredientes="""
- 300g de arroz arborio
- 250g de champiñones frescos
- 1 litro de caldo de verduras
- 1 cebolla pequeña
- 1 diente de ajo
- 50g de queso parmesano rallado
- 50ml de vino blanco
- 2 cucharadas de mantequilla
- Sal y pimienta al gusto
""",
    instrucciones="""
1. Pica la cebolla y el ajo finamente. Limpia y corta los champiñones en láminas.
2. Sofríe la cebolla y el ajo en una sartén con mantequilla hasta que estén transparentes.
3. Añade los champiñones y cocina unos minutos.
4. Incorpora el arroz y rehoga hasta que los granos estén translúcidos.
5. Vierte el vino blanco y deja que se evapore.
6. Añade el caldo caliente poco a poco, removiendo constantemente, hasta que el arroz esté cremoso y al dente.
7. Agrega el queso parmesano, mezcla y sirve caliente.
""",
    imagen="risotto.jpg"
)

Receta.objects.create(
    nombre="Ensalada César",
    ingredientes="""
- 1 lechuga romana
- 2 pechugas de pollo
- 100g de crutones
- 50g de queso parmesano en lascas
- 4 cucharadas de aderezo César
- Sal y pimienta al gusto
""",
    instrucciones="""
1. Asa las pechugas de pollo, salpimenta y corta en tiras.
2. Lava y trocea la lechuga romana.
3. Mezcla la lechuga con el aderezo César en un bol grande.
4. Añade el pollo, los crutones y el queso parmesano.
5. Remueve suavemente y sirve inmediatamente.
""",
    imagen="ensalada.jpg"
)