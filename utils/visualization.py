"""https://github.com/microsoft/graphrag/blob/main/examples_notebooks/community_contrib/yfiles-jupyter-graphs/graph-visualization.ipynb"""

def show_graph(result):
    """Visualize the result context with yfiles-jupyter-graphs."""
    from yfiles_jupyter_graphs import GraphWidget

    if (
        "entities" not in result.context_data
        or "relationships" not in result.context_data
    ):
        msg = "The passed results do not contain 'entities' or 'relationships'"
        raise ValueError(msg)

    # converts the entities dataframe to a list of dicts for yfiles-jupyter-graphs
    def convert_entities_to_dicts(df):
        """Convert the entities dataframe to a list of dicts for yfiles-jupyter-graphs."""
        nodes_dict = {}
        for _, row in df.iterrows():
            # Create a dictionary for each row and collect unique nodes
            node_id = row["entity"]
            if node_id not in nodes_dict:
                nodes_dict[node_id] = {
                    "id": node_id,
                    "properties": row.to_dict(),
                }
        return list(nodes_dict.values())

    # converts the relationships dataframe to a list of dicts for yfiles-jupyter-graphs
    def convert_relationships_to_dicts(df):
        """Convert the relationships dataframe to a list of dicts for yfiles-jupyter-graphs."""
        relationships = []
        for _, row in df.iterrows():
            # Create a dictionary for each row
            relationships.append({
                "start": row["source"],
                "end": row["target"],
                "properties": row.to_dict(),
            })
        return relationships

    w = GraphWidget()
    # use the converted data to visualize the graph
    w.nodes = convert_entities_to_dicts(result.context_data["entities"])
    w.edges = convert_relationships_to_dicts(result.context_data["relationships"])
    w.directed = True
    # show title on the node
    w.node_label_mapping = "entity"
    # use weight for edge thickness
    w.edge_thickness_factor_mapping = "weight"
    display(w)


show_graph(result)