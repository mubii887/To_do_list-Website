import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for styling
st.markdown("""
    <style>
        .big-title {
            text-align: center;
            font-size: 36px;
            color: #4CAF50;
        }
        .task-container {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        .completed-task {
            text-decoration: line-through;
            color: grey;
        }
        .button-container {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='big-title'>📝 Enhanced To-Do List</h1>", unsafe_allow_html=True)

if "tasks" not in st.session_state:
    st.session_state.tasks = []
    st.session_state.completed_tasks = []

new_task = st.text_input("Enter a new task:", placeholder="Type here...")
if st.button("➕ Add Task", use_container_width=True):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.rerun()

st.subheader("📌 Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    with st.container():
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
        with col1:
            st.markdown(f"<div class='task-container'>{task}</div>", unsafe_allow_html=True)
        with col2:
            if st.button("✅ Done", key=f"done_{i}"):
                st.session_state.completed_tasks.append(task)
                st.session_state.tasks.pop(i)
                st.rerun()
        with col3:
            if st.button("❌ Remove", key=f"del_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

st.subheader("✔️ Completed Tasks:")
for task in st.session_state.completed_tasks:
    st.markdown(f"<div class='task-container completed-task'>✅ {task}</div>", unsafe_allow_html=True)

if st.button("🗑️ Clear Completed Tasks", use_container_width=True):
    st.session_state.completed_tasks = []
    st.rerun()

st.write("⚠️ Tasks will reset when the page refreshes.")

