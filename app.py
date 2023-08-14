import streamlit as st



st.set_page_config(
    page_title="Clasificador Tiempos",
    page_icon="🌏",
)

st.write("# Clasificador de Tiempos para tramites segun Municipio y Tipo👋")

st.sidebar.success("Select un item")
st.markdown(
    """
    ## Descripción de una base de datos sobre patrones de flujo en tuberías 🚰  🧢  

    Una base de datos sobre patrones de flujo en tuberías se centra en el estudio del comportamiento de los fluidos en este contexto. Esta base de datos describe seis patrones de flujo comunes encontrados en las tuberías:

    | Sigla | Descripción |
    |-------|-------------|
    | DB    | Flujo de burbujas dispersas. Gas fluye en pequeñas burbujas dispersas dentro de un líquido, moviéndose aleatoriamente y con distribución irregular. Se encuentra en sistemas de aireación y procesos de mezcla. |
    | SS    | Flujo estratificado uniforme. Dos fluidos diferentes, como líquido y gas, fluyen paralelos sin mezclarse, con una superficie de separación plana y uniforme. Común en torres de destilación y sistemas de absorción. |
    | SW    | Flujo estratificado ondulado. Similar al SS, pero la superficie de separación es ondulada debido a la acción de la gravedad y la fricción entre los fluidos. Se encuentra en tuberías inclinadas y procesos de transferencia de calor. |
    | A     | Flujo anular. Líquido fluye en el centro y gas en la periferia de la tubería, formando un anillo alrededor del líquido con superficie de separación curva. Común en sistemas de inyección de gas y torres de absorción. |
    | I     | Flujo intermitente. Diferentes patrones de flujo se alternan a lo largo de la tubería. Común en tuberías con cambios de sección y en procesos de transporte de líquidos y gases. |
    | B     | Flujo de burbujas. Gas fluye en grandes burbujas dentro del líquido, formando un patrón distintivo y moviéndose hacia la superficie de la tubería. Se encuentra en sistemas de agitación y procesos de aireación. |

    Estos patrones de flujo se caracterizan por diferentes configuraciones y propiedades. La base de datos proporciona información detallada sobre cada patrón, incluyendo características, aplicaciones y ejemplos. También puede contener datos experimentales, simulaciones numéricas y modelos teóricos relacionados con el comportamiento de los fluidos en tuberías.

    La base de datos también registra los siguientes datos de entrada que se utilizan para caracterizar y clasificar el flujo en la tubería:

    | Campo        | Descripción                                            |
    |--------------|--------------------------------------------------------|
    | Vsl          | Velocidad del líquido en la tubería.                   |
    | Vsg          | Velocidad del gas en la tubería.                       |
    | VisL         | Viscosidad del líquido.                                |
    | VisG         | Viscosidad del gas.                                    |
    | DenL         | Densidad del líquido.                                  |
    | DenG         | Densidad del gas.                                      |
    | ST           | Tensión superficial entre el líquido y el gas.          |
    | Ang          | Ángulo de inclinación de la tubería (en caso de SW).    |
    | ID           | Diámetro interno de la tubería.                         |
    | FlowPattern  | Patrón de flujo observado en la tubería.                |

    Estos datos se almacenan en la base de datos junto con información adicional relacionada con las propiedades y características de cada patrón de flujo.

    La base de datos permite realizar consultas, análisis y visualización de los datos, facilitando el estudio de los patrones de flujo y la identificación de relaciones y tendencias entre los datos de entrada y los patrones observados. También puede ser utilizada para desarrollar modelos predictivos o algoritmos de clasificación que permitan predecir el patrón de flujo en función de los datos de entrada proporcionados.
    
    

    """
)