from llama_parse import LlamaParse
import os

def parse_pdfs(pdfs_root_path):
    for file in os.listdir(pdfs_root_path):
        if file.endswith(".pdf"):
            try:
                print(f"Converting {file} to markdown")
                md_text = LlamaParse(
                    result_type="markdown", 
                    verbose=True,
                    use_vendor_multimodal_model=True,
                    vendor_multimodal_model_name="openai-gpt-4o-mini",
                    vendor_multimodal_api_key=os.getenv("OPENAI_API_KEY"),
                    language="en",
                    numWorkers=5).load_data(pdfs_root_path + file)
                combined_md_text = "\n\n".join([doc.text for doc in md_text])
                md_file_path = pdfs_root_path + file.replace(".pdf", ".md")
                print(f"Saving markdown to {md_file_path}")
                with open(md_file_path, "w") as f:
                    f.write(combined_md_text)
                print(f"Successfully converted {file}")
            except Exception as e:
                print(f"Error converting {file}: {e}")