# graph.py
from langgraph.graph import StateGraph, END
from state import ComplaintState
from agents import understanding_agent, location_agent, clustering_agent, routing_agent

# State makinesini oluştur
workflow = StateGraph(ComplaintState)

# Düğümleri (Node) ekle
workflow.add_node("understand", understanding_agent)
workflow.add_node("locate", location_agent)
workflow.add_node("embed_and_cluster", clustering_agent)
workflow.add_node("route", routing_agent)

# Akışı birbirine bağla (Edge)
workflow.set_entry_point("understand")
workflow.add_edge("understand", "locate")
workflow.add_edge("locate", "embed_and_cluster")
workflow.add_edge("embed_and_cluster", "route")
workflow.add_edge("route", END)

# Grafı derle
mavi_masa_app = workflow.compile()