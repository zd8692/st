import streamlit as st
import numpy as np
import time

def generate_random_data():
    """生成随机数据模拟动态更新"""
    return [
        {"id": chr(65+i), "value": np.random.randint(10, 100), "group": np.random.randint(1, 4)}
        for i in range(6)
    ]

# 在Streamlit中嵌入HTML和JavaScript代码
html_template = """
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <div id="d3-bubble"></div>

    <script>
        var width = 600;
        var height = 400;
        var svg = d3.select("#d3-bubble").append("svg")
            .attr("width", width)
            .attr("height", height);
        var color = d3.scaleOrdinal(d3.schemeCategory10);

        function update(data) {
            var simulation = d3.forceSimulation(data)
                .force("charge", d3.forceManyBody().strength(5))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collision", d3.forceCollide().radius(function(d) {
                    return d.value + 5;
                }));

            simulation.on("tick", function() {
                var u = svg.selectAll("circle").data(data);

                u.enter()
                    .append("circle")
                    .attr("r", function(d) { return d.value; })
                    .style("fill", function(d) { return color(d.group); })
                    .merge(u)
                    .attr("cx", function(d) { return d.x; })
                    .attr("cy", function(d) { return d.y; });

                u.exit().remove();
            });
        }

        // 暴露update函数到全局，以便Python调用
        window.update = update;
    </script>
</body>
"""

# 初始渲染
st.components.v1.html(html_template, height=500)

# 动态更新数据
while True:
    # 生成新的随机数据
    new_data = generate_random_data()
    # 调用JavaScript的更新函数
    st.components.v1.html(
        f"<script>window.update({new_data});</script>",
        height=0,  # 设置为0，因为不需要显示额外的内容
    )
    time.sleep(1)  # 每秒更新一次
