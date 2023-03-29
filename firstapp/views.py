from firstapp.models import Category, Content, Website
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def read_websites(request):
    list_websites = Website.objects.all()
    return render(request, 'firstapp/websites.html', context={
        'List_Websites': list_websites,
    })


def read_contents(request):
    list_contents = Content.objects.all()
    return render(request, 'firstapp/contents.html', context={
        'List_Contents': list_contents,
    })


def contents_by_web(request, pk):
    list_contents = Content.objects.filter(website=pk)
    return render(request, 'firstapp/contents_by_web.html', {
        'List_Contents': list_contents,
    })


def contents_by_web_2(request, id):
    website = Website.objects.get(id=id)
    return render(request, 'firstapp/contents_by_web_2.html', {
        'Website': website,
    })








# def read_websites1(request):
#     category = Category.objects.all()
#     for c in category.Website_set.all:
#         print(c)
#     return render(request, 'firstapp/websites.html', context={
#         # 'List_Websites': list_websites,
#     })


# ================== CÁC BUỔI TRƯỚC
def index(request):
    noi_dung = "Chào mừng các bạn đến với lớp Web Django"
    return HttpResponse(noi_dung)


def trang_chu(request):
    return render(request, 'firstapp/index.html')


def tham_so(request, so_1, so_2):
    noi_dung = "Đang hiển thị số %i và %i" % (so_1, so_2)
    return HttpResponse(noi_dung)


def read_year(request, year):
    noi_dung = 'Năm đang nhập là %s' % year
    return HttpResponse(noi_dung)


def read_month_year(request, month, year):
    noi_dung = '%s / %s' % (month, year)
    return HttpResponse(noi_dung)


def ngay_hien_hanh(request):
    noi_dung = "Ngày hiện hành: %s" % (datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    return render(request, 'firstapp/ngay_hien_hanh.html',
                  {'NgayHienHanh': noi_dung})


def tinh_diem_tb(request):
    diem_tb = 4.9
    text = 'Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add'
    return render(request, 'firstapp/demo_tag.html',
                  {'DiemTB': diem_tb,
                   'Text': text})


def cart(request):
    ds_san_pham = [
        {
            'Ten_san_pham': 'Sản phẩm 1',
            'So_luong': 2,
            'Don_gia': 15000
        },
        {
            'Ten_san_pham': 'Sản phẩm 2',
            'So_luong': 6,
            'Don_gia': 20000
        },
        {
            'Ten_san_pham': 'Sản phẩm 3',
            'So_luong': 1,
            'Don_gia': 35000
        },
    ]
    return render(request, 'firstapp/demo_tag_2.html', {'DSSanPham': ds_san_pham})


def create_category(request):

    if request.POST.get('btnCreate'):
        # Gán biến
        category_name = request.POST.get('category_name')
        c = Category(name=category_name)
        c.save()

    # if request.POST.__get__('btnCreate'):
    #     print(133)
    return render(request, 'firstapp/create_category.html')


def demo_ckeditor(request):

    # if request.POST.get('btnCreate'):
    #     # Gán biến
    #     category_name = request.POST.get('category_name')
    #     c = Category(name=category_name)
    #     c.save()

    return render(request, 'firstapp/demo_ckeditor.html')


