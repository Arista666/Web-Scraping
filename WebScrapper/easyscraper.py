#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EasyScraper - Aplikasi Web Scraping yang User-Friendly
Dibuat untuk memudahkan scraping website tanpa coding
"""

import os
import sys
import subprocess
import importlib
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import time
import json
from datetime import datetime
import webbrowser
from urllib.robotparser import RobotFileParser

# Fungsi untuk mengecek dan menginstall dependencies
def check_and_install_dependencies():
    """Mengecek dan menginstall dependencies yang diperlukan"""
    required_packages = {
        'requests': 'requests',
        'beautifulsoup4': 'bs4',
        'selenium': 'selenium',
        'pandas': 'pandas',
        'lxml': 'lxml',
        'openpyxl': 'openpyxl'
    }
    
    missing_packages = []
    
    for package, import_name in required_packages.items():
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Menginstall dependencies: {', '.join(missing_packages)}")
        for package in missing_packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("Semua dependencies telah diinstall!")

# Install dependencies jika belum ada
try:
    check_and_install_dependencies()
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from urllib.parse import urljoin, urlparse
    import re
except Exception as e:
    print(f"Error installing dependencies: {e}")
    input("Tekan Enter untuk keluar...")
    sys.exit(1)

class EasyScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EasyScraper v1.0 - Web Scraping Made Easy")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Variabel
        self.scraped_data = []
        self.is_scraping = False
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()
        self.center_window()
        
    def center_window(self):
        """Menempatkan window di tengah layar"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
    
    def create_widgets(self):
        """Membuat semua widget GUI"""
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        title_label = ttk.Label(header_frame, text="EasyScraper", 
                               font=('Arial', 16, 'bold'))
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, 
                                  text="Scraping website jadi mudah - tanpa coding! ヾ(≧▽≦*)o",
                                  font=('Arial', 10))
        subtitle_label.pack()
        
        # Notebook untuk tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Tab 1: Simple Scraper
        self.create_simple_tab(notebook)
        
        # Tab 2: Advanced Scraper
        self.create_advanced_tab(notebook)
        
        # Tab 3: Robots.txt Checker
        self.create_robots_tab(notebook)
        
        # Tab 4: Data Viewer
        self.create_data_tab(notebook)
        
        # Tab 5: Help
        self.create_help_tab(notebook)
        
        # Status bar
        self.status_var = tk.StringVar(value="Siap untuk scraping")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief='sunken', anchor='w')
        status_bar.pack(fill='x', side='bottom')
    
    def create_simple_tab(self, notebook):
        """Tab untuk scraping sederhana"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="📄 Simple Scraper")
        
        # URL Input
        url_frame = ttk.LabelFrame(frame, text="Website URL", padding=10)
        url_frame.pack(fill='x', padx=10, pady=5)
        
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(url_frame, textvariable=self.url_var, font=('Arial', 10))
        url_entry.pack(fill='x', pady=5)
        
        # URL controls
        url_controls = ttk.Frame(url_frame)
        url_controls.pack(fill='x', pady=5)
        
        ttk.Button(url_controls, text="🤖 Check Robots.txt", 
                  command=self.check_robots_txt).pack(side='left', padx=5)
        
        ttk.Button(url_controls, text="🌐 Open in Browser", 
                  command=self.open_in_browser).pack(side='left', padx=5)
        
        # Robots.txt status
        self.robots_status = ttk.Label(url_frame, text="", foreground="blue")
        self.robots_status.pack(anchor='w', pady=2)
        
        # Contoh URLs
        examples_frame = ttk.Frame(url_frame)
        examples_frame.pack(fill='x')
        
        ttk.Label(examples_frame, text="Contoh:", font=('Arial', 9)).pack(side='left')
        
        example_urls = [
            "https://quotes.toscrape.com",
            "https://books.toscrape.com",
            "https://httpbin.org/html"
        ]
        
        for url in example_urls:
            btn = ttk.Button(examples_frame, text=url.split('//')[1][:20] + "...", 
                           command=lambda u=url: self.url_var.set(u))
            btn.pack(side='left', padx=2)
        
        # Target Elements
        target_frame = ttk.LabelFrame(frame, text="Apa yang ingin di-scrape?", padding=10)
        target_frame.pack(fill='x', padx=10, pady=5)
        
        target_options = [
            ("📝 Semua teks", "text"),
            ("🔗 Semua link", "links"),
            ("🖼️ Semua gambar", "images"),
            ("📊 Tabel", "tables"),
            ("📋 Custom CSS Selector", "custom")
        ]
        
        self.target_var = tk.StringVar(value="text")
        
        for text, value in target_options:
            ttk.Radiobutton(target_frame, text=text, variable=self.target_var, 
                           value=value).pack(anchor='w')
        
        # Custom selector
        self.custom_frame = ttk.Frame(target_frame)
        ttk.Label(self.custom_frame, text="CSS Selector:").pack(anchor='w')
        self.custom_selector = tk.StringVar()
        ttk.Entry(self.custom_frame, textvariable=self.custom_selector).pack(fill='x')
        
        # Bind radio button untuk show/hide custom selector
        for widget in target_frame.winfo_children():
            if isinstance(widget, ttk.Radiobutton):
                widget.configure(command=self.toggle_custom_selector)
        
        # Controls
        control_frame = ttk.Frame(frame)
        control_frame.pack(fill='x', padx=10, pady=10)
        
        self.scrape_btn = ttk.Button(control_frame, text="🚀 Mulai Scraping", 
                                    command=self.start_simple_scraping,
                                    style='Accent.TButton')
        self.scrape_btn.pack(side='left', padx=5)
        
        self.stop_btn = ttk.Button(control_frame, text="⏹️ Stop", 
                                  command=self.stop_scraping, state='disabled')
        self.stop_btn.pack(side='left', padx=5)
        
        ttk.Button(control_frame, text="💾 Export Data", 
                  command=self.export_data).pack(side='right', padx=5)
        
        ttk.Button(control_frame, text="🗑️ Clear", 
                  command=self.clear_data).pack(side='right', padx=5)
        
        # Progress
        self.progress = ttk.Progressbar(frame, mode='indeterminate')
        self.progress.pack(fill='x', padx=10, pady=5)
        
        # Results
        results_frame = ttk.LabelFrame(frame, text="Hasil Scraping", padding=10)
        results_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=10)
        self.results_text.pack(fill='both', expand=True)
    
    def create_advanced_tab(self, notebook):
        """Tab untuk scraping advanced"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="⚙️ Advanced")
        
        # Settings
        settings_frame = ttk.LabelFrame(frame, text="Pengaturan Advanced", padding=10)
        settings_frame.pack(fill='x', padx=10, pady=5)
        
        # Headers
        headers_frame = ttk.Frame(settings_frame)
        headers_frame.pack(fill='x', pady=5)
        
        ttk.Label(headers_frame, text="User Agent:").pack(anchor='w')
        self.user_agent = tk.StringVar(value="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        ttk.Entry(headers_frame, textvariable=self.user_agent).pack(fill='x')
        
        # Delay
        delay_frame = ttk.Frame(settings_frame)
        delay_frame.pack(fill='x', pady=5)
        
        ttk.Label(delay_frame, text="Delay antar request (detik):").pack(side='left')
        self.delay_var = tk.StringVar(value="1")
        ttk.Entry(delay_frame, textvariable=self.delay_var, width=10).pack(side='left', padx=5)
        
        # Multiple URLs
        urls_frame = ttk.LabelFrame(frame, text="Multiple URLs", padding=10)
        urls_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        ttk.Label(urls_frame, text="Masukkan URLs (satu per baris):").pack(anchor='w')
        self.urls_text = scrolledtext.ScrolledText(urls_frame, height=8)
        self.urls_text.pack(fill='both', expand=True, pady=5)
        
        # Advanced controls
        adv_control_frame = ttk.Frame(frame)
        adv_control_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(adv_control_frame, text="🚀 Scrape Multiple URLs", 
                  command=self.start_advanced_scraping).pack(side='left', padx=5)
        
        ttk.Button(adv_control_frame, text="📁 Load URLs from File", 
                  command=self.load_urls_from_file).pack(side='left', padx=5)
    
    def create_robots_tab(self, notebook):
        """Tab untuk robots.txt checker"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="🤖 Robots.txt")
        
        # URL input for robots checking
        robots_url_frame = ttk.LabelFrame(frame, text="Check Robots.txt", padding=10)
        robots_url_frame.pack(fill='x', padx=10, pady=5)
        
        self.robots_url_var = tk.StringVar()
        robots_url_entry = ttk.Entry(robots_url_frame, textvariable=self.robots_url_var, font=('Arial', 10))
        robots_url_entry.pack(fill='x', pady=5)
        
        robots_controls = ttk.Frame(robots_url_frame)
        robots_controls.pack(fill='x', pady=5)
        
        ttk.Button(robots_controls, text="🔍 Check Robots.txt", 
                  command=self.check_robots_detailed).pack(side='left', padx=5)
        
        ttk.Button(robots_controls, text="🌐 View Robots.txt", 
                  command=self.view_robots_txt).pack(side='left', padx=5)
        
        ttk.Button(robots_controls, text="📋 Batch Check", 
                  command=self.batch_check_robots).pack(side='left', padx=5)
        
        # Results display
        results_frame = ttk.LabelFrame(frame, text="Robots.txt Analysis", padding=10)
        results_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.robots_results = scrolledtext.ScrolledText(results_frame, height=20, font=('Consolas', 10))
        self.robots_results.pack(fill='both', expand=True)
        
        # Quick tips
        tips_frame = ttk.LabelFrame(frame, text="Quick Tips", padding=10)
        tips_frame.pack(fill='x', padx=10, pady=5)
        
        tips_text = """💡 Tips:
• Selalu cek robots.txt sebelum scraping: domain.com/robots.txt
• Perhatikan "Disallow:" - jangan scrape path yang dilarang
• Ikuti "Crawl-delay:" - set delay sesuai yang diminta
• "User-agent: *" berlaku untuk semua bot termasuk EasyScraper"""
        
        ttk.Label(tips_frame, text=tips_text, justify='left').pack(anchor='w')
    
    def create_data_tab(self, notebook):
        """Tab untuk melihat dan mengelola data"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="📊 Data Viewer")
        
        # Data summary
        summary_frame = ttk.LabelFrame(frame, text="Ringkasan Data", padding=10)
        summary_frame.pack(fill='x', padx=10, pady=5)
        
        self.data_summary = ttk.Label(summary_frame, text="Belum ada data")
        self.data_summary.pack(anchor='w')
        
        # Data table
        table_frame = ttk.LabelFrame(frame, text="Data Table", padding=10)
        table_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview untuk tabel
        columns = ('No', 'URL', 'Type', 'Content', 'Timestamp')
        self.data_tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.data_tree.heading(col, text=col)
            self.data_tree.column(col, width=100)
        
        # Scrollbar untuk treeview
        scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.data_tree.yview)
        self.data_tree.configure(yscrollcommand=scrollbar.set)
        
        self.data_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Export options
        export_frame = ttk.Frame(frame)
        export_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(export_frame, text="📄 Export CSV", 
                  command=lambda: self.export_data('csv')).pack(side='left', padx=5)
        
        ttk.Button(export_frame, text="📊 Export Excel", 
                  command=lambda: self.export_data('excel')).pack(side='left', padx=5)
        
        ttk.Button(export_frame, text="📋 Export JSON", 
                  command=lambda: self.export_data('json')).pack(side='left', padx=5)
    
    def create_help_tab(self, notebook):
        """Tab bantuan dan tutorial"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="❓ Help")
        
        help_text = """
🕷️ PANDUAN EASYSCRAPER

📋 CARA PENGGUNAAN:

1. SIMPLE SCRAPER:
   • Masukkan URL website yang ingin di-scrape
   • Pilih jenis data (teks, link, gambar, tabel, atau custom)
   • Klik "Mulai Scraping"
   • Lihat hasil di tab "Data Viewer"

2. ADVANCED SCRAPER:
   • Atur User Agent dan delay
   • Masukkan multiple URLs
   • Scrape banyak website sekaligus

3. EXPORT DATA:
   • CSV: untuk analisis data
   • Excel: untuk laporan
   • JSON: untuk developer

🎯 TIPS:
   • Gunakan delay untuk website yang sensitif
   • Custom CSS selector untuk data spesifik
   • Cek robots.txt sebelum scraping
   • Respect website's terms of service

⚠️ PERINGATAN:
   • Selalu patuhi terms of service website
   • Jangan spam request ke server
   • Gunakan delay yang wajar
   • Beberapa website mungkin memblokir scraping

🔧 CSS SELECTOR EXAMPLES:
   • h1, h2, h3 → Semua heading
   • .class-name → Element dengan class tertentu
   • #id-name → Element dengan ID tertentu
   • a[href] → Semua link
   • img[src] → Semua gambar

📞 SUPPORT:
   Jika ada masalah, pastikan:
   • Koneksi internet stabil
   • URL valid dan dapat diakses
   • Website tidak memblokir scraping
        """
        
        help_display = scrolledtext.ScrolledText(frame, wrap='word')
        help_display.pack(fill='both', expand=True, padx=10, pady=10)
        help_display.insert('1.0', help_text)
        help_display.configure(state='disabled')
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        ttk.Button(btn_frame, text="🌐 CSS Selector Tester", 
                  command=lambda: webbrowser.open("https://www.w3schools.com/cssref/trysel.asp")).pack(side='left', padx=5)
        
        ttk.Button(btn_frame, text="📖 Regex Tester", 
                  command=lambda: webbrowser.open("https://regex101.com/")).pack(side='left', padx=5)
    
    def toggle_custom_selector(self):
        """Toggle custom selector visibility"""
        if self.target_var.get() == "custom":
            self.custom_frame.pack(fill='x', pady=5)
        else:
            self.custom_frame.pack_forget()
    
    def update_status(self, message):
        """Update status bar"""
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def start_simple_scraping(self):
        """Memulai simple scraping"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Masukkan URL terlebih dahulu!")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            self.url_var.set(url)
        
        self.is_scraping = True
        self.scrape_btn.configure(state='disabled')
        self.stop_btn.configure(state='normal')
        self.progress.start()
        
        # Jalankan scraping di thread terpisah
        thread = threading.Thread(target=self.scrape_website, args=(url,))
        thread.daemon = True
        thread.start()
    
    def start_advanced_scraping(self):
        """Memulai advanced scraping"""
        urls_text = self.urls_text.get('1.0', 'end-1c').strip()
        if not urls_text:
            messagebox.showerror("Error", "Masukkan URLs terlebih dahulu!")
            return
        
        urls = [url.strip() for url in urls_text.split('\n') if url.strip()]
        if not urls:
            messagebox.showerror("Error", "Tidak ada URL valid!")
            return
        
        self.is_scraping = True
        self.progress.start()
        
        # Jalankan scraping di thread terpisah
        thread = threading.Thread(target=self.scrape_multiple_websites, args=(urls,))
        thread.daemon = True
        thread.start()
    
    def scrape_website(self, url):
        """Scraping satu website"""
        try:
            self.update_status(f"Scraping {url}...")
            
            headers = {'User-Agent': self.user_agent.get()}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            target_type = self.target_var.get()
            
            results = []
            
            if target_type == "text":
                # Ambil semua teks
                for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div']):
                    text = element.get_text(strip=True)
                    if text and len(text) > 10:  # Filter teks pendek
                        results.append({
                            'type': 'text',
                            'content': text,
                            'tag': element.name
                        })
            
            elif target_type == "links":
                # Ambil semua link
                for link in soup.find_all('a', href=True):
                    href = urljoin(url, link['href'])
                    text = link.get_text(strip=True)
                    results.append({
                        'type': 'link',
                        'content': href,
                        'text': text
                    })
            
            elif target_type == "images":
                # Ambil semua gambar
                for img in soup.find_all('img', src=True):
                    src = urljoin(url, img['src'])
                    alt = img.get('alt', '')
                    results.append({
                        'type': 'image',
                        'content': src,
                        'alt': alt
                    })
            
            elif target_type == "tables":
                # Ambil tabel
                for i, table in enumerate(soup.find_all('table')):
                    try:
                        df = pd.read_html(str(table))[0]
                        results.append({
                            'type': 'table',
                            'content': df.to_string(),
                            'table_id': i
                        })
                    except:
                        pass
            
            elif target_type == "custom":
                # Custom CSS selector
                selector = self.custom_selector.get().strip()
                if selector:
                    for element in soup.select(selector):
                        content = element.get_text(strip=True) if element.string else str(element)
                        results.append({
                            'type': 'custom',
                            'content': content,
                            'selector': selector
                        })
            
            # Simpan hasil
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for result in results:
                self.scraped_data.append({
                    'url': url,
                    'timestamp': timestamp,
                    **result
                })
            
            # Update UI
            self.root.after(0, self.update_results_display)
            self.root.after(0, lambda: self.update_status(f"Berhasil scraping {len(results)} item dari {url}"))
            
        except Exception as e:
            self.root.after(0, lambda: self.update_status(f"Error: {str(e)}"))
            self.root.after(0, lambda: messagebox.showerror("Error", f"Gagal scraping {url}:\n{str(e)}"))
        
        finally:
            self.root.after(0, self.scraping_finished)
    
    def scrape_multiple_websites(self, urls):
        """Scraping multiple websites"""
        try:
            delay = float(self.delay_var.get())
        except:
            delay = 1
        
        total_results = 0
        
        for i, url in enumerate(urls):
            if not self.is_scraping:
                break
            
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            try:
                self.update_status(f"Scraping {i+1}/{len(urls)}: {url}")
                
                headers = {'User-Agent': self.user_agent.get()}
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Simple scraping - ambil teks dan link
                results = []
                
                # Teks
                for element in soup.find_all(['p', 'h1', 'h2', 'h3']):
                    text = element.get_text(strip=True)
                    if text and len(text) > 20:
                        results.append({
                            'type': 'text',
                            'content': text[:200] + '...' if len(text) > 200 else text
                        })
                
                # Links
                for link in soup.find_all('a', href=True):
                    href = urljoin(url, link['href'])
                    text = link.get_text(strip=True)
                    if text:
                        results.append({
                            'type': 'link',
                            'content': href,
                            'text': text
                        })
                
                # Simpan hasil
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for result in results:
                    self.scraped_data.append({
                        'url': url,
                        'timestamp': timestamp,
                        **result
                    })
                
                total_results += len(results)
                
                # Delay antar request
                if i < len(urls) - 1:
                    time.sleep(delay)
                
            except Exception as e:
                self.root.after(0, lambda e=e, u=url: messagebox.showwarning("Warning", f"Gagal scraping {u}:\n{str(e)}"))
        
        # Update UI
        self.root.after(0, self.update_results_display)
        self.root.after(0, lambda: self.update_status(f"Selesai! Total {total_results} item dari {len(urls)} website"))
        self.root.after(0, self.scraping_finished)
    
    def stop_scraping(self):
        """Stop scraping"""
        self.is_scraping = False
        self.scraping_finished()
    
    def scraping_finished(self):
        """Reset UI setelah scraping selesai"""
        self.is_scraping = False
        self.scrape_btn.configure(state='normal')
        self.stop_btn.configure(state='disabled')
        self.progress.stop()
    
    def update_results_display(self):
        """Update tampilan hasil"""
        # Clear previous results
        self.results_text.delete('1.0', 'end')
        
        # Show latest results
        recent_data = self.scraped_data[-50:]  # Show last 50 items
        
        for i, item in enumerate(recent_data, 1):
            self.results_text.insert('end', f"{i}. [{item['type'].upper()}] {item['url']}\n")
            self.results_text.insert('end', f"   {item['content'][:100]}...\n\n")
        
        # Update data table
        self.update_data_table()
        
        # Update summary
        total_items = len(self.scraped_data)
        unique_urls = len(set(item['url'] for item in self.scraped_data))
        self.data_summary.configure(text=f"Total: {total_items} items dari {unique_urls} website")
    
    def update_data_table(self):
        """Update data table"""
        # Clear existing data
        for item in self.data_tree.get_children():
            self.data_tree.delete(item)
        
        # Add new data
        for i, item in enumerate(self.scraped_data, 1):
            content = item['content'][:50] + "..." if len(item['content']) > 50 else item['content']
            self.data_tree.insert('', 'end', values=(
                i, item['url'], item['type'], content, item['timestamp']
            ))
    
    def export_data(self, format_type='csv'):
        """Export data ke berbagai format"""
        if not self.scraped_data:
            messagebox.showinfo("Info", "Belum ada data untuk di-export!")
            return
        
        try:
            if format_type == 'csv':
                filename = filedialog.asksaveasfilename(
                    defaultextension=".csv",
                    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
                )
                if filename:
                    df = pd.DataFrame(self.scraped_data)
                    df.to_csv(filename, index=False, encoding='utf-8-sig')
                    messagebox.showinfo("Success", f"Data berhasil di-export ke {filename}")
            
            elif format_type == 'excel':
                filename = filedialog.asksaveasfilename(
                    defaultextension=".xlsx",
                    filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
                )
                if filename:
                    df = pd.DataFrame(self.scraped_data)
                    df.to_excel(filename, index=False)
                    messagebox.showinfo("Success", f"Data berhasil di-export ke {filename}")
            
            elif format_type == 'json':
                filename = filedialog.asksaveasfilename(
                    defaultextension=".json",
                    filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
                )
                if filename:
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.scraped_data, f, indent=2, ensure_ascii=False)
                    messagebox.showinfo("Success", f"Data berhasil di-export ke {filename}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Gagal export data: {str(e)}")
    
    def clear_data(self):
        """Clear semua data"""
        if messagebox.askyesno("Konfirmasi", "Hapus semua data scraped?"):
            self.scraped_data.clear()
            self.results_text.delete('1.0', 'end')
            self.update_data_table()
            self.data_summary.configure(text="Belum ada data")
            self.update_status("Data cleared")
    
    def load_urls_from_file(self):
        """Load URLs dari file"""
        filename = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.urls_text.delete('1.0', 'end')
                    self.urls_text.insert('1.0', content)
                messagebox.showinfo("Success", "URLs berhasil dimuat!")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat file: {str(e)}")
    
    def check_robots_txt(self):
        """Check robots.txt untuk URL yang dimasukkan"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Masukkan URL terlebih dahulu!")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            # Parse domain from URL
            from urllib.parse import urlparse
            parsed = urlparse(url)
            robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
            
            self.update_status(f"Checking robots.txt: {robots_url}")
            
            # Check robots.txt in separate thread
            thread = threading.Thread(target=self._check_robots_thread, args=(robots_url, url))
            thread.daemon = True
            thread.start()
            
        except Exception as e:
            self.robots_status.configure(text=f"❌ Error checking robots.txt: {str(e)}", 
                                        foreground="red")
    
    def _check_robots_thread(self, robots_url, target_url):
        """Check robots.txt in background thread"""
        try:
            rp = RobotFileParser()
            rp.set_url(robots_url)
            rp.read()
            
            # Check if our user agent can fetch the URL
            user_agent = self.user_agent.get() if hasattr(self, 'user_agent') else '*'
            can_fetch = rp.can_fetch(user_agent, target_url)
            
            # Get crawl delay
            crawl_delay = rp.crawl_delay(user_agent)
            
            # Get request rate
            request_rate = rp.request_rate(user_agent)
            
            # Update UI in main thread
            if can_fetch:
                status_text = "✅ Scraping diizinkan"
                color = "green"
            else:
                status_text = "❌ Scraping tidak diizinkan"
                color = "red"
            
            if crawl_delay:
                status_text += f" | Delay: {crawl_delay}s"
                # Auto-update delay in advanced settings
                if hasattr(self, 'delay_var'):
                    self.root.after(0, lambda: self.delay_var.set(str(max(float(self.delay_var.get()), crawl_delay))))
            
            if request_rate:
                status_text += f" | Rate: {request_rate.requests}/{request_rate.seconds}s"
            
            self.root.after(0, lambda: self.robots_status.configure(text=status_text, foreground=color))
            self.root.after(0, lambda: self.update_status(f"Robots.txt checked: {'Allowed' if can_fetch else 'Blocked'}"))
            
            # Show detailed robots.txt info
            if not can_fetch:
                self.root.after(0, lambda: self._show_robots_warning(robots_url))
                
        except Exception as e:
            error_text = f"⚠️ Tidak bisa mengakses robots.txt"
            self.root.after(0, lambda: self.robots_status.configure(text=error_text, foreground="orange"))
            self.root.after(0, lambda: self.update_status("Robots.txt tidak tersedia (mungkin tidak ada)"))
    
    def _show_robots_warning(self, robots_url):
        """Show warning dialog when robots.txt blocks scraping"""
        result = messagebox.askyesno(
            "Robots.txt Warning", 
            f"Website ini melarang scraping menurut robots.txt!\n\n"
            f"URL: {robots_url}\n\n"
            f"⚠️ Melanjutkan scraping mungkin melanggar terms of service.\n\n"
            f"Mau lihat robots.txt lengkap?"
        )
        
        if result:
            webbrowser.open(robots_url)
    
    def open_in_browser(self):
        """Buka URL di browser"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Masukkan URL terlebih dahulu!")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        webbrowser.open(url)
    
    def check_robots_detailed(self):
        """Detailed robots.txt check"""
        url = self.robots_url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Masukkan URL atau domain!")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        self.robots_results.delete('1.0', 'end')
        self.robots_results.insert('end', f"🔍 Checking robots.txt for: {url}\n")
        self.robots_results.insert('end', "=" * 60 + "\n\n")
        
        thread = threading.Thread(target=self._detailed_robots_check, args=(url,))
        thread.daemon = True
        thread.start()
    
    def _detailed_robots_check(self, url):
        """Detailed robots.txt analysis"""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
            
            # Fetch robots.txt content
            headers = {'User-Agent': 'EasyScraper/1.0'}
            response = requests.get(robots_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                robots_content = response.text
                
                # Parse with RobotFileParser
                rp = RobotFileParser()
                rp.set_url(robots_url)
                rp.read()
                
                # Analysis
                result = f"✅ Robots.txt found at: {robots_url}\n\n"
                result += "📄 ROBOTS.TXT CONTENT:\n"
                result += "-" * 40 + "\n"
                result += robots_content + "\n"
                result += "-" * 40 + "\n\n"
                
                # Test different paths
                test_paths = ['/', '/admin/', '/api/', '/search/', '/user/', '/private/']
                user_agents = ['*', 'EasyScraper', 'Googlebot']
                
                result += "🧪 ACCESS ANALYSIS:\n"
                result += "-" * 40 + "\n"
                
                for user_agent in user_agents:
                    result += f"\nUser-agent: {user_agent}\n"
                    for path in test_paths:
                        test_url = f"{parsed.scheme}://{parsed.netloc}{path}"
                        can_fetch = rp.can_fetch(user_agent, test_url)
                        status = "✅ ALLOWED" if can_fetch else "❌ BLOCKED"
                        result += f"  {path:<12} → {status}\n"
                    
                    # Check crawl delay
                    crawl_delay = rp.crawl_delay(user_agent)
                    if crawl_delay:
                        result += f"  Crawl-delay: {crawl_delay} seconds\n"
                
                # Recommendations
                result += "\n🎯 RECOMMENDATIONS:\n"
                result += "-" * 40 + "\n"
                
                main_allowed = rp.can_fetch('*', url)
                if main_allowed:
                    result += "✅ Main page scraping is ALLOWED\n"
                    
                    crawl_delay = rp.crawl_delay('*')
                    if crawl_delay:
                        result += f"⏱️  Recommended delay: {crawl_delay} seconds\n"
                        result += f"🔧 Set delay in Advanced tab to {crawl_delay}+ seconds\n"
                    else:
                        result += "⏱️  No specific delay required, but use 1-2 seconds minimum\n"
                else:
                    result += "❌ Main page scraping is BLOCKED\n"
                    result += "⚠️  Scraping this site may violate their terms of service\n"
                    result += "💡 Consider contacting website owner for permission\n"
                
                # Find sitemaps
                sitemap_lines = [line for line in robots_content.split('\n') 
                               if line.strip().lower().startswith('sitemap:')]
                if sitemap_lines:
                    result += "\n🗺️  SITEMAPS FOUND:\n"
                    for sitemap in sitemap_lines:
                        result += f"   {sitemap.strip()}\n"
                
            elif response.status_code == 404:
                result = f"ℹ️  No robots.txt found at: {robots_url}\n\n"
                result += "This means:\n"
                result += "✅ No specific restrictions (generally safe to scrape)\n"
                result += "✅ Still recommended to use delays and be respectful\n"
                result += "⚠️  Check website terms of service\n"
                
            else:
                result = f"⚠️  Error accessing robots.txt: HTTP {response.status_code}\n"
                result += f"URL: {robots_url}\n"
                
        except Exception as e:
            result = f"❌ Error checking robots.txt: {str(e)}\n"
            result += f"URL: {robots_url}\n"
        
        # Update UI
        self.root.after(0, lambda: self.robots_results.delete('1.0', 'end'))
        self.root.after(0, lambda: self.robots_results.insert('1.0', result))
    
    def view_robots_txt(self):
        """Open robots.txt in browser"""
        url = self.robots_url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Masukkan URL!")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        from urllib.parse import urlparse
        parsed = urlparse(url)
        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
        webbrowser.open(robots_url)
    
    def batch_check_robots(self):
        """Batch check robots.txt for multiple domains"""
        domains_text = """masukkan domain (satu per baris):
tokopedia.com
shopee.co.id
bukalapak.com
blibli.com
lazada.co.id"""
        
        domains = tk.simpledialog.askstring(
            "Batch Robots.txt Check",
            "Masukkan domains (satu per baris):",
            initialvalue=domains_text
        )
        
        if not domains:
            return
        
        domain_list = [d.strip() for d in domains.split('\n') if d.strip()]
        if not domain_list:
            return
        
        self.robots_results.delete('1.0', 'end')
        self.robots_results.insert('end', f"🔍 Batch checking {len(domain_list)} domains...\n")
        self.robots_results.insert('end', "=" * 60 + "\n\n")
        
        thread = threading.Thread(target=self._batch_robots_check, args=(domain_list,))
        thread.daemon = True
        thread.start()
    
    def _batch_robots_check(self, domains):
        """Batch robots.txt check"""
        results = []
        
        for i, domain in enumerate(domains, 1):
            if not domain.startswith(('http://', 'https://')):
                domain = 'https://' + domain
            
            try:
                from urllib.parse import urlparse
                parsed = urlparse(domain)
                robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
                
                self.root.after(0, lambda d=domain: self.update_status(f"Checking {d}..."))
                
                rp = RobotFileParser()
                rp.set_url(robots_url)
                rp.read()
                
                can_fetch = rp.can_fetch('*', domain)
                crawl_delay = rp.crawl_delay('*')
                
                status = "✅ ALLOWED" if can_fetch else "❌ BLOCKED"
                delay_info = f" (delay: {crawl_delay}s)" if crawl_delay else ""
                
                result = f"{i:2d}. {parsed.netloc:<25} → {status}{delay_info}\n"
                results.append(result)
                
                # Update UI progressively
                self.root.after(0, lambda r=result: self.robots_results.insert('end', r))
                
                time.sleep(1)  # Be respectful
                
            except Exception as e:
                result = f"{i:2d}. {domain:<25} → ❌ ERROR: {str(e)}\n"
                results.append(result)
                self.root.after(0, lambda r=result: self.robots_results.insert('end', r))
        
        # Summary
        allowed = sum(1 for r in results if "✅ ALLOWED" in r)
        blocked = sum(1 for r in results if "❌ BLOCKED" in r)
        errors = sum(1 for r in results if "❌ ERROR" in r)
        
        summary = f"\n📊 SUMMARY:\n"
        summary += f"✅ Allowed: {allowed}\n"
        summary += f"❌ Blocked: {blocked}\n"
        summary += f"⚠️  Errors: {errors}\n"
        
        self.root.after(0, lambda: self.robots_results.insert('end', summary))
        self.root.after(0, lambda: self.update_status("Batch robots.txt check completed"))

def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    # Cek Python version
    if sys.version_info < (3, 6):
        print("ERROR: Python 3.6 atau lebih baru diperlukan!")
        input("Tekan Enter untuk keluar...")
        return
    
    try:
        root = tk.Tk()
        app = EasyScraperApp(root)
        
        # Icon dan styling
        try:
            root.iconbitmap('')  # Default icon
        except:
            pass
        
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menjalankan aplikasi: {str(e)}")

if __name__ == "__main__":
    print("🕷️ EasyScraper - Starting Application...")
    print("Checking dependencies...")
    main()