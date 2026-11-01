"""Valoraciones voluntarias. SPDX-License-Identifier: AGPL-3.0-only."""
import argparse
import json

def validate_score(value):
    text = str(value).strip()
    if not text.isascii() or not text.isdigit() or not 1 <= int(text) <= 100:
        raise ValueError('La valoración debe ser un entero entre 1 y 100.')
    return int(text)

def proposal(name, first, second, agreed=False):
    name = str(name).strip()
    if not name or len(name)>120:
        raise ValueError('La propuesta debe tener entre 1 y 120 caracteres.')
    if agreed is not True:
        raise ValueError('Ambas personas deben aceptar libremente.')
    a,b=validate_score(first),validate_score(second)
    return {'name':name,'a':a,'b':b,'score':min(a,b)}

def main():
    parser=argparse.ArgumentParser(description='Valora una propuesta compartida. No crea obligaciones.')
    parser.add_argument('name');parser.add_argument('first');parser.add_argument('second')
    parser.add_argument('--aceptado',action='store_true',help='Ambas personas aceptan libremente la propuesta.')
    args=parser.parse_args()
    try: result=proposal(args.name,args.first,args.second,args.aceptado)
    except ValueError as error: parser.error(str(error))
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
