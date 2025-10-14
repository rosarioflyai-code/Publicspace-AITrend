import os
from jinja2 import Environment, FileSystemLoader
import markdown
from datetime import datetime

def main():
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    post_template = env.get_template('post.html')
    list_template = env.get_template('list.html')

    # Create the output directory if it doesn't exist
    if not os.path.exists('site'):
        os.makedirs('site')

    # Read all the posts
    posts = []
    for filename in os.listdir('content'):
        if filename.endswith('.md'):
            filepath = os.path.join('content', filename)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Extract title from the first line
            title = content.split('\n')[0].replace('#', '').strip()
            
            # Convert markdown to html
            html_content = markdown.markdown(content)

            # Parse date from filename
            date_str = filename.replace('.md', '')
            date = datetime.strptime(date_str, '%Y-%m-%d')

            posts.append({
                'title': title,
                'date': date,
                'content': html_content,
                'filename': filename.replace('.md', '.html')
            })

    # Sort posts by date
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Generate individual post pages
    for post in posts:
        year = post['date'].year
        month = post['date'].month
        day = post['date'].day

        # Create directories
        if not os.path.exists(f'site/{year}/{month:02d}/{day:02d}') :
            os.makedirs(f'site/{year}/{month:02d}/{day:02d}')

        # Generate post page
        output_path = f'site/{year}/{month:02d}/{day:02d}/index.html'
        with open(output_path, 'w') as f:
            f.write(post_template.render(title=post['title'], date=post['date'].strftime('%B %d, %Y'), content=post['content']))

    # Generate index pages
    generate_index_pages(posts, list_template)


def generate_index_pages(posts, list_template):
    # Group posts by year, month
    tree = {}
    for post in posts:
        year = post['date'].year
        month = post['date'].month
        day = post['date'].day
        if year not in tree:
            tree[year] = {}
        if month not in tree[year]:
            tree[year][month] = []
        tree[year][month].append(post)

    # Generate root index page (list of years)
    years = [{'name': year, 'url': f'/{year}/'} for year in sorted(tree.keys(), reverse=True)]
    with open('site/index.html', 'w') as f:
        f.write(list_template.render(title='Years', items=years))

    # Generate year index pages (list of months)
    for year, months in tree.items():
        if not os.path.exists(f'site/{year}') :
            os.makedirs(f'site/{year}')
        
        month_items = [{'name': datetime(year, month, 1).strftime('%B'), 'url': f'/{year}/{month:02d}/'} for month in sorted(months.keys(), reverse=True)]
        with open(f'site/{year}/index.html', 'w') as f:
            f.write(list_template.render(title=f'Months in {year}', items=month_items))

        # Generate month index pages (list of days)
        for month, day_posts in months.items():
            if not os.path.exists(f'site/{year}/{month:02d}') :
                os.makedirs(f'site/{year}/{month:02d}')

            day_items = [{'name': post['date'].strftime('%d'), 'url': f'/{year}/{month:02d}/{post["date"].day:02d}/'} for post in sorted(day_posts, key=lambda x: x['date'], reverse=True)]
            with open(f'site/{year}/{month:02d}/index.html', 'w') as f:
                f.write(list_template.render(title=f'Days in {datetime(year, month, 1).strftime("%B")} {year}', items=day_items))


if __name__ == '__main__':
    main()
