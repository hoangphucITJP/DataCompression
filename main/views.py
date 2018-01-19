from django.http import HttpResponse
from django.template import loader
from .form import UploadFileForm
import os
from ipware.ip import get_ip
import datetime
import pytz
from .Encode import Encode
from .Decode import Decode
import operator
import zipfile
import time

output = ''

path = os.path.dirname(__file__)

# Create your views here.
def index(request):
    write_log(request, 'accessed index')
    print("index")
    template = loader.get_template('main/index.html')
    form = UploadFileForm(request.POST, request.FILES)
    return HttpResponse(template.render({'form':form}))

def upload(request):
    if request.method != 'POST':
        return HttpResponse('What\'s up?')

    write_log(request, 'uploaded ' + str(len(request.FILES.getlist('file[]'))) + ' file(s) for ' + request.POST['algo'] + ' ' + request.POST['mode'])
    #Save files
    inputPath = path + '/data/input/'
    filenames = [handle_uploaded_file(i, inputPath) for i in request.FILES.getlist('file[]')]

    #Process file
    outputPath = path + '/data/output/'
    global output
    print(request.POST['algo'])
    dispatcher = {'Encoding': Encode, 'Decoding': Decode}
    process_times = []
    for i in filenames:
        source = inputPath + i
        destination = outputPath + i
        t0 = time.process_time()
        dispatcher[request.POST['mode']](source, destination, request.POST['algo'])
        t1 = time.process_time()
        t = (t1 - t0)*1000
        t = "{0:.2f}".format(round(t, 2))
        process_times.append(str(t))

    #Calculate compression ratio
    input_file_size = [os.path.getsize(inputPath + i) for i in filenames]
    output_file_size = [os.path.getsize(outputPath + i) for i in filenames]
    multidivide = lambda a,b: map(operator.truediv, a,b)
    if (request.POST['mode'] == 'Decoding'):
        compression_ratio = list(multidivide(output_file_size, input_file_size))
    else:
        compression_ratio = list(multidivide(input_file_size, output_file_size))


    #Send response
    process_times = ['<td>' + i + '</td>' for i in process_times]
    compression_ratio = ['<td>' + str("{0:.2f}".format(round(i, 2))) + '</td>' for i in compression_ratio]
    downloadlinks = ['<td><a href="/main/download?file=' + i + '" download="' + i + '">Tải xuống</a></td>' for i in filenames]
    multiconcent = lambda a,b: map(str.__add__, a,b)

    response = list(multiconcent(compression_ratio, process_times))
    response = list(multiconcent(response, downloadlinks))
    response = '<tr>' + '</tr><tr>'.join(response) + '</tr>'
    response = '<table><tr><th>Compression ratio</th><th>Processed time (ms)</th><th>Processed file</th><tr>' + response + '</table>'
    return HttpResponse(response)

def log(request):
    with open(path + "/data/log.txt", "r") as client_ips:
        res = client_ips.read()
        client_ips.close()
    res = res.replace('\n', '<br>')
    return HttpResponse(res)

def download(request):
    try:
        filename = request.GET['file']
    except:
        return HttpResponse("What's up?")
    file = open(path + '/data/output/' + filename, mode='rb')
    data = file.read()
    file.close()
    return HttpResponse(data)

def handle_uploaded_file(f, savepath):
    filename = f.name
    fullname = savepath + filename
    print(fullname)
    with open(fullname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename

def write_log(request, msg):
    ip = get_ip(request)
    if ip is not None:
        tzCode = ' '.join(pytz.country_timezones['vn'])
        tz = pytz.timezone(tzCode)
        time = datetime.datetime.now(tz)
        time = time.strftime('%d-%m-%Y %H:%M:%S')
        with open(path + "/data/log.txt", "a") as client_ips:
            client_ips.write(ip + ' ' + time + ': ' + msg + '\n')
            client_ips.close()