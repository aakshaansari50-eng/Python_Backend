def video_views(titles, views):
    result = [
        (title, round(count / 1000) * 1000)
        for title, count in zip(titles, views)
    ]
    return result


titles = ["Python Tutorial", "Django Tutorial", "MySQL Tutorial"]
views = [125600, 98750, 456780]

print(video_views(titles, views))