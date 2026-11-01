from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_harry_potter_bot():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://www.harrypotter.com/pt/login")
        driver.get("https://harrypottershop.com/collections/gifts/Under-$10")
        
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.grid__item, .product-card, .grid-view-item, .card-wrapper")))
        
        produtos_elementos = driver.find_elements(By.CSS_SELECTOR, "li.grid__item, .product-card, .grid-view-item, .card-wrapper")
        
        if not produtos_elementos:
            produtos_elementos = driver.find_elements(By.CSS_SELECTOR, "a[href*='/products/']")

        lista_produtos = []
        
        for item in produtos_elementos:
            try:
                titulo = ""
                for seletor_titulo in [".card__heading", ".product-card__title", "h3", "a.full-unstyled-link", ".title"]:
                    try:
                        el = item.find_element(By.CSS_SELECTOR, seletor_titulo)
                        if el.text.strip():
                            titulo = el.text.strip()
                            break
                    except Exception:
                        pass
                
                preco = ""
                for seletor_preco in [".price", ".money", ".price-item", ".price__regular"]:
                    try:
                        el = item.find_element(By.CSS_SELECTOR, seletor_preco)
                        if el.text.strip():
                            preco = el.text.strip()
                            break
                    except Exception:
                        pass
                
                if titulo:
                    produto_dict = {"titulo": titulo, "Preço": preco if preco else "Preço não informado"}
                    if produto_dict not in lista_produtos:
                        lista_produtos.append(produto_dict)
                        
            except Exception:
                continue

        print("\n" + "="*40)
        print("📊 RESULTADOS DA COLETA (WEB SCRAPING)")
        print("="*40)
        
        for idx, produto in enumerate(lista_produtos, 1):
            print(f"{idx}. Título: {produto['titulo']} | Preço: {produto['Preço']}")
            
        print("="*40)
        print(f"✨ Quantidade total de produtos coletados: {len(lista_produtos)}")
        print("="*40)

    except Exception as e:
        print(f"❌ Ocorreu um erro durante a execução do bot: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_harry_potter_bot()