"""
4. Escribe un programa capaz de quitar los comentarios de un programa de Java.

Se utilizaría de la siguiente manera:

python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

Por ejemplo:

python quita-comentarios.py Holav1.java Holav2.java

crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.

P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de error
correspondiente.

"""
import sys

program_with_comentaries = sys.argv[1]
program_without_comentaries = sys.argv[2]

with open(program_with_comentaries, 'rt') as f:
    with open(program_without_comentaries, 'wt') as w:
        lines = f.read()
        while True:
            if lines.find('/*') == -1 and lines.find('*/') == -1:
                break
            lines = lines[:lines.find('/*')] + '' + lines[2 + lines.find('*/'):]
        while True:
            if lines.find('//') == -1:
                break
            lines = lines[:lines.find('//')] + '' + lines[lines.find('\n', lines.find('//')):]
        w.writelines(lines)
