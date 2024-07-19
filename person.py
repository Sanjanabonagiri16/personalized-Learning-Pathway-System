import pandas as pd

# Load the data
data = pd.read_csv('users.csv')

# Display the data
print(data)
# Convert skills, preferences, and progress to lists
data['skills'] = data['skills'].apply(lambda x: x.split(';'))
data['preferences'] = data['preferences'].apply(lambda x: x.split(';'))
data['progress'] = data['progress'].astype(int)

# Display the preprocessed data
print(data)
# Function to recommend next steps based on skills and preferences
def recommend_next_steps(user_id):
    user = data[data['user_id'] == user_id].iloc[0]
    skills = user['skills']
    preferences = user['preferences']
    progress = user['progress']

    # Dummy recommendations based on skills and preferences
    recommendations = []
    if 'Python' in skills:
        recommendations.append('Advanced Python Course')
    if 'Data Science' in skills:
        recommendations.append('Data Science Project')
    if 'Video' in preferences:
        recommendations.append('Watch Data Science Tutorials on YouTube')
    if 'Interactive' in preferences:
        recommendations.append('Interactive Python Challenges')
    
    return recommendations

# Test the recommendation system
user_id = 1
recommendations = recommend_next_steps(user_id)
print(f'Recommendations for user {user_id}: {recommendations}')
def main():
    print("Welcome to the Personalized Learning Pathway System!")
    user_id = int(input("Enter your user ID: "))
    recommendations = recommend_next_steps(user_id)
    
    print(f'\nRecommendations for user {user_id}:')
    for rec in recommendations:
        print(f'- {rec}')

if __name__ == "__main__":
    main()
