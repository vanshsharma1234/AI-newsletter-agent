import streamlit as st
from agent import NewsletterAgent


# PAGE CONFIG
st.set_page_config(
    page_title="AI Newsletter Agent",
    page_icon="📰",
    layout="wide"
)


# SESSION STATE
if "summary_generated" not in st.session_state:
    st.session_state.summary_generated = False

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "goal" not in st.session_state:
    st.session_state.goal = ""

if "newsletter_html" not in st.session_state:
    st.session_state.newsletter_html = ""

if "articles" not in st.session_state:
    st.session_state.articles = []


# TITLE
st.title("AI Newsletter Agent")

st.write(
    "Autonomous AI agent that researches, summarizes, and generates newsletters automatically."
)

st.divider()


# USER INPUT
goal = st.text_input(
    "Enter Goal",
    "Create a weekly newsletter on latest AI agent news."
)


# HUMAN LOOP TOGGLE
human_mode = st.toggle(
    "Human-in-the-Loop Mode"
)


# RUN BUTTON
if st.button("Run Agent"):

    try:

        agent = NewsletterAgent()

        status = st.status(
            "Initializing Agent...",
            expanded=True
        )

        with status:

            st.info("Planning workflow...")

            result = agent.run_newsletter_agent(goal)

            st.session_state.articles = result["articles"]

            st.success("Research phase completed")

            st.info("Collecting relevant articles...")

            st.success(
                f"{len(result['articles'])} articles collected"
            )

            st.info("Generating summaries...")

            st.success("Summaries generated successfully")

            # SHOW WORKFLOW
            with st.expander("View Agent Workflow"):

                for log in result["logs"]:
                    st.write(log)

            # SHOW ARTICLES
            with st.expander("View Retrieved Articles"):

                for idx, article in enumerate(result["articles"], start=1):

                    st.markdown(
                        f"**{idx}. {article['title']}**"
                    )

            # HUMAN MODE
            if human_mode:

                st.session_state.summary_generated = True
                st.session_state.summary = result["summary"]
                st.session_state.goal = goal

                status.update(
                    label="Waiting for Human Approval...",
                    state="running"
                )

            # AUTONOMOUS MODE
            else:

                st.info("Generating newsletter layout...")

                final_result = agent.generate_final_newsletter(
                    result["summary"],
                    goal
                )

                st.session_state.newsletter_html = final_result["newsletter"]

                st.success("Newsletter generated successfully")

                status.update(
                    label="Process Completed Successfully",
                    state="complete"
                )

                st.subheader("Generated Newsletter")

                st.components.v1.html(
                    final_result["newsletter"],
                    height=700,
                    scrolling=True
                )

                # DOWNLOAD BUTTON
                st.download_button(
                    label="Download Newsletter",
                    data=st.session_state.newsletter_html,
                    file_name="newsletter.html",
                    mime="text/html"
                )

                st.caption(
                    "Open the downloaded HTML file in browser and press Cmd + P to print."
                )

    except Exception as e:

        st.error(f"Error: {e}")


# HUMAN APPROVAL SECTION
if st.session_state.summary_generated:

    st.divider()

    st.subheader("Human Approval Required")

    st.write(st.session_state.summary)

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Approve"):

            try:

                agent = NewsletterAgent()

                status = st.status(
                    "Finalizing Newsletter...",
                    expanded=True
                )

                with status:

                    st.info("Generating final newsletter...")

                    final_result = agent.generate_final_newsletter(
                        st.session_state.summary,
                        st.session_state.goal
                    )

                    st.session_state.newsletter_html = final_result["newsletter"]

                    st.success("Newsletter finalized")

                    status.update(
                        label="Newsletter Approved & Generated",
                        state="complete"
                    )

                st.subheader("Generated Newsletter")

                st.components.v1.html(
                    final_result["newsletter"],
                    height=700,
                    scrolling=True
                )

                # DOWNLOAD BUTTON
                st.download_button(
                    label="Download Newsletter",
                    data=st.session_state.newsletter_html,
                    file_name="newsletter.html",
                    mime="text/html"
                )

                st.caption(
                    "Open the downloaded HTML file in browser and press Cmd + P to print."
                )

                st.session_state.summary_generated = False

            except Exception as e:

                st.error(f"Error: {e}")

    with col2:

        if st.button("Reject"):

            st.warning(
                "Newsletter generation stopped by user."
            )

            st.session_state.summary_generated = False