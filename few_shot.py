import json
import pandas as pd

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)   # load posts automatically when class is initialized

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

        # Flatten JSON into a DataFrame
        self.df = pd.json_normalize(posts)

        # Categorize post length
        self.df["length"] = self.df["line_count"].apply(self.categorize_length)

        # Collect all unique tags
        all_tags = self.df["tags"].apply(lambda x: x).sum()
        self.unique_tags = set(all_tags)

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"
        
    def get_tags(self):
        return self.unique_tags
    
    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient="records")  # fixed `record` → `records`

if __name__ == "__main__":
    fs = FewShotPosts("data/processed_posts.json")
    posts = fs.get_filtered_posts("Medium", "English", "Job Search")
    print(posts)
