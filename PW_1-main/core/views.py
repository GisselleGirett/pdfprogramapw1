
from django.shortcuts import render, redirect
from .models import PDF
import PyPDF2
import re

def import_success(request):
    return render(request, 'import_success.html')


def importar_pdf(request):
    if request.method == 'POST' and request.FILES.getlist('pdf_files'):
        pdf_files = request.FILES.getlist('pdf_files')

        for pdf_file in pdf_files:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page = pdf_reader.pages[0]
            text = page.extract_text()

            page_2 = pdf_reader.pages[1]  # Segunda página
            text_page_2 = page_2.extract_text()
            
            page_3 = pdf_reader.pages[2]  # Tercera página
            text_page_3 = page_3.extract_text()

            page_4 = pdf_reader.pages[3]  # Tercera página
            text_page_4 = page_4.extract_text()
                                    
            nombre_archivo = pdf_file.name
            materia = None
            codigo = None
            carrera = None
            objetivos_text = None
            fundamentacion_text = None
            contenido_text_page_2 = None 
            metodologia_text_page_2 = None
            evaluacion_text_page_3 = None
            bibliografia_text_page_4 = None

            # Extraer datos del PDF
            materia_match = re.search(r'Nombre\s*de\s*la\s*Materia\s*:\s*(.*)', text)
            materia = materia_match.group(1).strip() if materia_match else None
            materia = re.sub(r'\.\s*$', '', materia) if materia else None

            codigo_match = re.search(r'Código\s*:\s*(.*)', text)
            codigo = codigo_match.group(1).strip().replace(" ", "") if codigo_match else None
            codigo = re.sub(r'\.\s*$', '', codigo) if codigo else None

            carrera_match = re.search(r'Carrera\s*:\s*(.*)', text)
            carrera = carrera_match.group(1).strip() if carrera_match else None
            carrera = re.sub(r'\.\s*$', '', carrera) if carrera else None

            fundamentacion_match = re.search(r'FUNDAMENTACIÓN\s*(?:\. )?(.*?)(?=III.|$)', text, re.DOTALL)
            fundamentacion_text = fundamentacion_match.group(1).strip() if fundamentacion_match else None
            
            objetivos_match = re.search(r'OBJETIVOS\s*(?:\. )?(.*?)(?=IV.|$)', text, re.DOTALL)
            objetivos_text = objetivos_match.group(1).strip() if objetivos_match else None

            contenido_match_page_2 = re.search(r'CONTENIDO\s*(?:\. )?(.*?)(?=V.|$)', text_page_2, re.DOTALL)
            contenido_text_page_2 = contenido_match_page_2.group(1).strip() if contenido_match_page_2 else None
            
            metodologia_match_page_2 = re.search(r'METODOLOGÍA\s*(?:\. )?(.*?)(?=VI.|$)', text_page_2, re.DOTALL)
            metodologia_text_page_2 =  metodologia_match_page_2.group(1).strip() if  metodologia_match_page_2 else None
            
            evaluacion_match_page_3 = re.search(r'1\s*(?:\. )?(.*?)(?=VII.|$)', text_page_3, re.DOTALL)
            evaluacion_text_page_3 =  evaluacion_match_page_3.group(1).strip() if  evaluacion_match_page_3 else None
            
            bibliografia_match_page_4 = re.search(r'BIBLIOGRAFÍA\s*(?:\. )?(.*?)(?=México |$)', text_page_4, re.DOTALL)
            bibliografia_text_page_4 =  bibliografia_match_page_4.group(1).strip() if  bibliografia_match_page_4 else None
            
            
            
            # Guardar en la base de datos
            pdf = PDF(nombre=nombre_archivo, materia=materia, carrera=carrera, codigo=codigo, objetivos=objetivos_text,fundamentacion=fundamentacion_text,
                      contenido= contenido_text_page_2,metodologia=metodologia_text_page_2,evaluacion=evaluacion_text_page_3,bibliografia=bibliografia_text_page_4)
            pdf.save()

        return redirect('import_success')
    return render(request, 'import_pdf.html')


