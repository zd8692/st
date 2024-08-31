import streamlit as st
import numpy as np
import json

# 生成随机数据的函数
def generate_random_data():
    return [
        {"id": chr(65+i), "value": np.random.randint(20, 80), "group": np.random.randint(1, 4)}
        for i in range(6)
    ]

# 初始数据
data = generate_random_data()

# 嵌入D3.js可视化的HTML和JavaScript代码
html_template = f"""
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <div id="d3-bubble"></div>

    <script>
        var data = {json.dumps(data)};
        var width = 600;
        var height = 400;
        var svg = d3.select("#d3-bubble").append("svg")
            .attr("width", width)
            .attr("height", height);
        var color = d3.scaleOrdinal(d3.schemeCategory10);

        function update(data) {{
            var simulation = d3.forceSimulation(data)
                .force("charge", d3.forceManyBody().strength(15))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collision", d3.forceCollide().radius(function(d) {{
                    return d.value;
                }}));

            simulation.on("tick", function() {{
                var u = svg.selectAll("circle").data(data, function(d) {{ return d.id; }});

                u.enter()
                    .append("circle")
                    .attr("r", function(d) {{ return d.value; }})
                    .style("fill", function(d) {{ return color(d.group); }})
                    .merge(u)
                    .attr("cx", function(d) {{ return d.x; }})
                    .attr("cy", function(d) {{ return d.y; }});

                u.exit().remove();
            }});
        }}

        update(data);

        window.update = update;
    </script>
</body>
"""

# 在Streamlit中渲染初始的HTML
st.components.v1.html(html_template, height=500)

# 添加一个按钮，用于触发数据更新
if st.button('Update Data'):
    new_data = generate_random_data()
    st.components.v1.html(
        f"<script>window.update({json.dumps(new_data)});</script>",
        height=0  # 设置为0，因为这里不需要显示额外的内容
    )
