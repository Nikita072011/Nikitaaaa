import streamlit as st
import string

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Application heading
st.title("🔐 Password Strength Checker")
st.write(
    "Check your password strength and get suggestions "
    "to create a stronger password."
)

st.info(
    "Your password is analyzed locally by this application "
    "and is not displayed as plain text."
)

# Password input field
password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Enter a password to check"
)

# Analyze password when entered
if password:
    # Check password criteria
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least one uppercase letter": any(
            char.isupper() for char in password
        ),
        "At least one lowercase letter": any(
            char.islower() for char in password
        ),
        "At least one number": any(
            char.isdigit() for char in password
        ),
        "At least one special character": any(
            char in string.punctuation for char in password
        )
    }

    # Calculate score out of 5
    score = sum(checks.values())

    # Determine strength
    if score <= 2:
        strength = "Weak"
        color = "🔴"
    elif score <= 4:
        strength = "Moderate"
        color = "🟠"
    else:
        strength = "Strong"
        color = "🟢"

    # Display results
    st.subheader("📊 Password Strength Analysis")

    st.metric("Password Strength Score", f"{score}/5")
    st.write(f"### {color} {strength} Password")

    # Visual progress bar
    st.write("Strength Progress")
    st.progress(score / 5)

    # Display checklist
    st.subheader("✅ Password Criteria Checklist")

    for criterion, satisfied in checks.items():
        if satisfied:
            st.success(f"✓ {criterion}")
        else:
            st.error(f"✗ {criterion}")

    # Display suggestions
    st.subheader("💡 Suggestions for Improvement")

    suggestions = {
        "At least 8 characters":
            "Use at least 8 characters.",
        "At least one uppercase letter":
            "Add an uppercase letter (A–Z).",
        "At least one lowercase letter":
            "Add a lowercase letter (a–z).",
        "At least one number":
            "Include a number (0–9).",
        "At least one special character":
            "Add a special character, such as !, @, #, or $."
    }

    missing = [
        suggestions[criterion]
        for criterion, satisfied in checks.items()
        if not satisfied
    ]

    if missing:
        for suggestion in missing:
            st.write(f"- {suggestion}")
    else:
        st.success(
            "Excellent! Your password satisfies all five criteria."
        )

    # Final message
    if strength == "Weak":
        st.warning(
            "Your password is weak. Follow the suggestions above "
            "to improve it."
        )
    elif strength == "Moderate":
        st.info(
            "Your password is moderately strong. "
            "Improve the missing criteria to reach a score of 5/5."
        )
    else:
        st.success(
            "Great job! Your password meets all five criteria."
        )

else:
    st.caption("Enter a password above to see your analysis.")
