import os
from web.enums.graphic_type import GraphicType

def call_graph_script(graphic_type: GraphicType, script_name):
    folder_path = {
        GraphicType.BarCharts: "web/graphs/BarCharts/",
        GraphicType.BoxPlots: "web/graphs/BoxPlots/",
        GraphicType.Histograms: "web/graphs/Histograms/",
        GraphicType.LineCharts: "web/graphs/LineCharts/",
        GraphicType.PieCharts: "web/graphs/PieCharts/",
        GraphicType.ScatterPlots: "/web/web/graphs/ScatterPlots/"
    }.get(graphic_type, "web/graphs/")

    script_path = os.path.join(folder_path, script_name + ".py")

    print(script_path)

    if os.path.isfile(script_path):
        os.system(f"python3 {script_path}")
    else:
        print(f"Script file '{script_name}' does not exist in the folder '{folder_path}'")