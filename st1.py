import streamlit as st
from graphviz import Digraph

def create_complex_decision_graph():
    dot = Digraph(comment='Company Decision Process', format='png')

    # 添加节点
    dot.node('Start', 'Start', shape='Mdiamond')
    dot.node('End', 'End', shape='Msquare')

    # 添加部门
    dot.node('HR', 'HR Department')
    dot.node('Eng', 'Engineering')
    dot.node('Sales', 'Sales Department')
    dot.node('Fin', 'Finance')

    # 添加决策节点
    dot.node('D1', 'Need New Software?', shape='diamond')
    dot.node('D2', 'Budget Approval', shape='diamond')
    dot.node('D3', 'Market Analysis', shape='diamond')
    dot.node('D4', 'HR Approval', shape='diamond')

    # 连接节点
    dot.edge('Start', 'D1')
    dot.edge('D1', 'HR', label='No')
    dot.edge('D1', 'D2', label='Yes')
    dot.edge('D2', 'Fin', label='No', color='red')
    dot.edge('D2', 'Eng', label='Yes')
    dot.edge('Eng', 'D3')
    dot.edge('D3', 'Sales')
    dot.edge('Sales', 'D4')
    dot.edge('HR', 'D4')
    dot.edge('D4', 'End', label='Approved')
    dot.edge('D4', 'Start', label='Rejected', color='red')

    # 将图表输出为PNG图片
    dot.render('complex_decision_graph')

    return dot

# 使用Graphviz绘制图
dot = create_complex_decision_graph()
st.graphviz_chart(dot)
