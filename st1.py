import streamlit as st
import json

# 初始化页面，并定义JavaScript部分，包括数据更新逻辑
html_content = """
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
    <div id="d3-bubble"></div>

    <script>
        var data = [
            {id: "A", value: 20, group: 1},
            {id: "B", value: 40, group: 2},
            {id: "C", value: 60, group: 3},
            {id: "D", value: 80, group: 1},
            {id: "E", value: 100, group: 2}
        ];
        var svg;
        var width = 600;
        var height = 400;
        var color = d3.scaleOrdinal(d3.schemeCategory10);

        document.addEventListener("DOMContentLoaded", function(event) {
            svg = d3.select("#d3-bubble").append("svg")
                .attr("width", width)
                .attr("height", height);

            update(data);

            // Set interval to update data every 2 seconds
            setInterval(function() {
                data.forEach(function(d) {
                    d.value = Math.random() * 100 + 20; // Randomize the radius
                });
                update(data);
            }, 2000);
        });

        function update(data) {
            var simulation = d3.forceSimulation(data)
                .force("charge", d3.forceManyBody().strength(15))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("collision", d3.forceCollide().radius(function(d) {
                    return d.value;
                }));

            simulation.on("tick", function() {
                var u = svg.selectAll("circle").data(data, function(d) { return d.id; });

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
    </script>
</body>
"""

# 使用Streamlit的html方法来加载初始页面
st.components.v1.html(html_content, height=500)
