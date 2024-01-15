from django.shortcuts import render, HttpResponse

nextID = 4
topics = [
    {'id':1,'title':'routing','body':'Routing is ..'},
    {'id':2,'title':'View','body':'View is ..'},
    {'id':3,'title':'Model','body':'Model is ..'},
]

def HTMLTemplate(article, id=None):
    global topics # topics를 전역변수로 지정
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ul = ''
    for topic in topics:
        ul += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ul}                
        </ul>
        {article}
        <ul>
            <li><a href = "/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request,id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article,id))

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
@csrf_exempt
def create(request):
    global nextID
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextID, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextID)
        nextID += 1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST': # delete는 POST 방식으로 접근할 때만 작동
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')
    
@csrf_exempt
def update(request,id):
    global topics
    if request.method == 'GET': # get으로 접속하면 update 텍스트 출력
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST': # post로 접속하면 수정된 상세페이지로 이동
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')
