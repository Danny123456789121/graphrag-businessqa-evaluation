import pandas as pd
import tiktoken
from graphrag.query.indexer_adapters import read_indexer_entities, read_indexer_reports, read_indexer_communities
#from graphrag.query.llm.oai.chat_openai import ChatOpenAI
from graphrag.query.llm.oai.typing import OpenaiApiType
from graphrag.query.structured_search.global_search.community_context import GlobalCommunityContext
from graphrag.query.structured_search.global_search.search import GlobalSearch

def setup_graphrag(model_name, llm, community_level, output_dir="./graphrag/output/"):
    token_encoder = tiktoken.encoding_for_model(model_name)
    community_df = pd.read_parquet(f"{output_dir}/create_final_communities.parquet")
    entity_df = pd.read_parquet(f"{output_dir}/create_final_nodes.parquet")
    report_df = pd.read_parquet(f"{output_dir}/create_final_community_reports.parquet")
    entity_embedding_df = pd.read_parquet(f"{output_dir}/create_final_entities.parquet")

    communities = read_indexer_communities(community_df, entity_df, report_df)
    reports = read_indexer_reports(report_df, entity_df, community_level)
    entities = read_indexer_entities(entity_df, entity_embedding_df, community_level)

    print(report_df.head())
    
    context_builder = GlobalCommunityContext(
        community_reports=reports,
        communities=communities,
        entities=entities,
        token_encoder=token_encoder,
    )

    context_builder_params = {
        "use_community_summary": False,
        "shuffle_data": True,
        "include_community_rank": True,
        "min_community_rank": 0,
        "community_rank_name": "rank",
        "include_community_weight": True,
        "community_weight_name": "occurrence weight",
        "normalize_community_weight": True,
        "max_tokens": 12_000,
        "context_name": "Reports",
    }

    map_llm_params = {
        "max_tokens": 1000,
        "temperature": 0.0,
        "response_format": {"type": "json_object"},
    }

    reduce_llm_params = {
        "max_tokens": 2000,
        "temperature": 0.0,
    }

    search_engine_global = GlobalSearch(
        llm=llm,
        context_builder=context_builder,
        token_encoder=token_encoder,
        max_data_tokens=12_000,
        map_llm_params=map_llm_params,
        reduce_llm_params=reduce_llm_params,
        allow_general_knowledge=False,
        json_mode=True,
        context_builder_params=context_builder_params,
        concurrent_coroutines=32,
        response_type="multiple paragraphs",
    )

    return search_engine_global