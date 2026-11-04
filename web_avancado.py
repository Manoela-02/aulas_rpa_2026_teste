import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def criar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def parte_1_selects(driver):
    logging.info("--- Iniciando Parte 1: Selects ---")
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    wait = WebDriverWait(driver, 10)
    select_element = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    select = Select(select_element)
    
    opcoes_texto = [op.text for op in select.options]
    logging.info(f"Opções disponíveis no dropdown: {opcoes_texto}")
    
    select.select_by_index(2)
    
    assert select.first_selected_option.text == "Option 2", f"Erro: Esperado 'Option 2', mas selecionado '{select.first_selected_option.text}'"
    logging.info("Validação Parte 1 concluída com sucesso: 'Option 2' selecionada corretamente.")

def parte_2_alerts(driver):
    logging.info("--- Iniciando Parte 2: Alerts JS ---")
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    
    botao_alert = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
    botao_alert.click()
    
    alert = wait.until(EC.alert_is_present())
    logging.info(f"Texto capturado do JS Alert: {alert.text}")
    alert.accept()
    
    resultado_1 = wait.until(EC.presence_of_element_located((By.ID, "result"))).text
    assert "You successfully clicked an alert" in resultado_1
    
    botao_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']")))
    botao_confirm.click()
    
    alert = wait.until(EC.alert_is_present())
    logging.info(f"Texto capturado do JS Confirm: {alert.text}")
    alert.dismiss()
    
    resultado_2 = wait.until(EC.presence_of_element_located((By.ID, "result"))).text
    assert resultado_2 == "You clicked: Cancel", f"Esperado 'You clicked: Cancel', obtido '{resultado_2}'"
    logging.info("Validação do JS Confirm (Cancel) bem-sucedida.")
    
    botao_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']")))
    botao_prompt.click()
    
    alert = wait.until(EC.alert_is_present())
    ra = "6326244"
    logging.info(f"Enviando RA {ra} para o JS Prompt...")
    alert.send_keys(ra)
    alert.accept()
    
    resultado_3 = wait.until(EC.presence_of_element_located((By.ID, "result"))).text
    assert ra in resultado_3, f"O RA {ra} não foi encontrado no resultado: '{resultado_3}'"
    logging.info("Validação Parte 2 concluída com sucesso (Alerts).")

def parte_3_iframes(driver):
    logging.info("--- Iniciando Parte 3: Iframes ---")
    driver.get("https://the-internet.herokuapp.com/iframe")
    wait = WebDriverWait(driver, 10)
    
    iframe_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.tox-edit-area > iframe, #mce_0_ifr")))
    driver.switch_to.frame(iframe_element)
    
    editor_body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    editor_body.clear()
    mensagem = "Automatizando com Selenium - RA: 6326244"
    editor_body.send_keys(mensagem)
    logging.info(f"Mensagem inserida no iframe: '{mensagem}'")
    
    driver.switch_to.default_content()
    
    cabecalho = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
    assert "An iFrame containing the TinyMCE WYSIWYG Editor" in cabecalho
    logging.info(f"Validação Parte 3 concluída com sucesso. Retornou ao contexto raiz. Título h3: '{cabecalho}'")

def parte_4_janelas(driver):
    logging.info("--- Iniciando Parte 4: Troca de Abas / Janelas ---")
    driver.get("https://the-internet.herokuapp.com/windows")
    wait = WebDriverWait(driver, 10)
    
    handle_original = driver.current_window_handle
    logging.info(f"Handle da aba original: {handle_original}")
    
    link_nova_janela = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    link_nova_janela.click()
    
    wait.until(EC.number_of_windows_to_be(2))
    
    handles_totais = driver.window_handles
    handle_novo = [h for h in handles_totais if h != handle_original][0]
    driver.switch_to.window(handle_novo)
    
    texto_nova_janela = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3"))).text
    assert texto_nova_janela == "New Window", f"Esperado 'New Window', obtido '{texto_nova_janela}'"
    logging.info("Validação na nova aba bem-sucedida ('New Window').")
    
    driver.close()
    driver.switch_to.window(handle_original)
    
    assert len(driver.window_handles) == 1, "Erro: Mais de uma aba aberta remanescente."
    titulo_original = driver.title
    assert "The Internet" in titulo_original
    logging.info("Validação Parte 4 concluída com sucesso. Foco e abas restabelecidos.")

def main():
    driver = criar_driver()
    try:
        parte_1_selects(driver)
        parte_2_alerts(driver)
        parte_3_iframes(driver)
        parte_4_janelas(driver)
        logging.info("🎉 Todas as partes do Lab 09 foram executadas com sucesso!")
    except Exception as e:
        logging.error(f"Erro fatal durante a execução dos testes: {e}")
        raise
    finally:
        driver.quit()
        logging.info("Driver encerrado com segurança.")

if __name__ == "__main__":
    main()