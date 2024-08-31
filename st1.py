import streamlit as st
import numpy as np
import json
import time

# 生成随机数据的函数
def generate_random_data():
    return [
        {"id": chr(65+i), "value": np.random.randint(20, 80), "group": np.random.randint(1, 4)}
        for i in range(6)
    ]

# 初始化容器
placeholder = st.empty()

# 嵌入D3.js可视化的HTML和JavaScript代码
html_template = """
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <div id="d3-bubble"></div>

    <script>
        var svg;
        var color = d3.scaleOrdinal(d3.schemeCategory10);
        var width = 600;
        var height = 400;

        function setup() {{
            svg = d3.select("#d3-bubble").append("svg")
                .attr("width", width)
                .attr("height", height);
        }}

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

        setup();
    </script>
"""

# 渲染初始HTML
placeholder.html(html_template, height=500)

# 持续更新数据
while True:
    # 生成新的随机数据
    new_data = generate_random_data()
    # 使用JavaScript更新D3图表
    update_script = f"<script>window.update({json.dumps(new_data)});</script>"
    placeholder.html(html_template + update_script, height=500)
    time.sleep(2)  # 每2秒更新一次
