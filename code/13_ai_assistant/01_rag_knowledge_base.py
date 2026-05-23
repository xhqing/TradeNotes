# Copyright (c) 2026 TradeNotes Authors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

try:
    from langchain.document_loaders import DirectoryLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma
    HAS_LANGCHAIN = True
except ImportError:
    HAS_LANGCHAIN = False
    print("langchain未安装，请运行: pip install langchain chromadb openai")

import os

if __name__ == '__main__' and HAS_LANGCHAIN:
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'code', 'output')
    notes_dir = os.path.join(OUTPUT_DIR, 'trading_notes')
    os.makedirs(notes_dir, exist_ok=True)

    sample_note = """
    交易日期: 2024-01-15
    标的: SPY
    策略: Bull Call Spread
    入场: 买440Call 卖450Call
    权利金: $3.50
    止损: 亏损2倍权利金
    情绪: 平静 (7/10)
    """
    with open(os.path.join(notes_dir, 'note_20240115.md'), 'w') as f:
        f.write(sample_note)

    loader = DirectoryLoader(notes_dir)
    docs = loader.load()
    print(f"加载了 {len(docs)} 个文档")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    print(f"分割为 {len(chunks)} 个文本块")

    print("\n注意: 需要设置 OPENAI_API_KEY 环境变量才能创建向量数据库")
    print("export OPENAI_API_KEY='your-api-key-here'")

    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=os.path.join(OUTPUT_DIR, 'db'))
        print("向量数据库创建成功!")

        results = vectorstore.similarity_search("SPY期权交易", k=2)
        for r in results:
            print(f"--- 匹配结果 ---\n{r.page_content[:200]}")
    else:
        print("未检测到OPENAI_API_KEY，跳过向量数据库创建")
