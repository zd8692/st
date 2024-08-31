import streamlit as st

# HTML模板，其中包括Mermaid.js库的加载和配置
html_template = """
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@8.13.5/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true});</script>
</head>
<body>
    <div class="mermaid">
        graph TD;
        Start(开始) --> Input{输入数据}
        Input --> Preprocess[预处理数据]
        Preprocess --> Analysis{数据分析}
        Analysis --> A[构建模型]
        Analysis --> B[统计分析]
        A --> A1[模型训练]
        A1 --> A2[模型评估]
        B --> B1[假设检验]
        B1 --> B2[结果解释]
        A2 --> Decision{决策制定}
        B2 --> Decision
        Decision --> End[结束]
        style Start fill:#f9f,stroke:#333,stroke-width:4px
        style End fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5
    </div>
</body>
</html>
"""

# 使用 Streamlit 的 HTML 组件展示 Mermaid 流程图
st.components.v1.html(html_template, height=800)
