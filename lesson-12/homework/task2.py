import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

db_name = "jobs.db"
url = "https://realpython.github.io/fake-jobs"

def create_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    ''')
    conn.commit()
    conn.close()

def scrape_jobs():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    
    for job in soup.find_all('div', class_='card-content'):
        title = job.find('h2', class_='title').text.strip()
        company = job.find('h3', class_='company').text.strip()
        location = job.find('p', class_='location').text.strip()
        description = job.find('div', class_='description').text.strip()
        application_link = job.find('a', text='Apply')['href'].strip()
        jobs.append((title, company, location, description, application_link))
    
    return jobs

def insert_or_update_jobs(jobs):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    for title, company, location, description, application_link in jobs:
        cursor.execute('''
            SELECT description, application_link FROM jobs 
            WHERE title = ? AND company = ? AND location = ?
        ''', (title, company, location))
        existing = cursor.fetchone()
        
        if existing:
            old_description, old_application_link = existing
            if old_description != description or old_application_link != application_link:
                cursor.execute('''
                    UPDATE jobs SET description = ?, application_link = ?
                    WHERE title = ? AND company = ? AND location = ?
                ''', (description, application_link, title, company, location))
        else:
            cursor.execute('''
                INSERT INTO jobs (title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, company, location, description, application_link))
    
    conn.commit()
    conn.close()

def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = "SELECT title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location = ?"
        params.append(location)
    if company:
        query += " AND company = ?"
        params.append(company)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def export_to_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)
    print(f"Exported {len(jobs)} jobs to {filename}")

if __name__ == "__main__":
    create_database()
    jobs = scrape_jobs()
    insert_or_update_jobs(jobs)
    print("Job listings updated successfully.")
    export_to_csv("filtered_jobs.csv", location="Remote")
