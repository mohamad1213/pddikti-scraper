from django.shortcuts import render
from execution.pddiktipy import api
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
import json

def home(request):
    template_name = 'templates/home.html'
    return render(request,template_name=template_name)

class DetailUnivDosen(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['universitas']
        pddikti_api = api()
        try:
            dosenuniv = pddikti_api.detail_univ_dosen_by_name(keyword=nama)
            jabatan_tetap = dosenuniv['tetap']['jumlah_dosen_jabatan'][
                'series']
            kelamin_tetap = dosenuniv['tetap']['jumlah_dosen_jenis_kelamin']
            jenjang_tetap = dosenuniv['tetap']['jumlah_dosen_jenjang'][
                'series']
            registrasi_tetap = dosenuniv['tetap']['jumlah_dosen_registrasi'][
                'series']
            jabatan = dosenuniv['tidak_tetap']['jumlah_dosen_jabatan'][
                'series']
            kelamin = dosenuniv['tidak_tetap']['jumlah_dosen_jenis_kelamin']
            jenjang = dosenuniv['tidak_tetap']['jumlah_dosen_jenjang'][
                'series']
            registrasi = dosenuniv['tidak_tetap']['jumlah_dosen_registrasi'][
                'series']
            output = {
                "dosen_tetap": {
                    "jumlah_dosen_jabatan": jabatan_tetap,
                    "jumlah_dosen_jenis_kelamin": kelamin_tetap,
                    "jumlah_dosen_jenjang": jenjang_tetap,
                    "jumlah_dosen_registrasi": registrasi_tetap
                },
                "dosen_tidak_tetap": {
                    "jumlah_dosen_jabatan": jabatan,
                    "jumlah_dosen_jenis_kelamin": kelamin,
                    "jumlah_dosen_jenjang": jenjang,
                    "jumlah_dosen_registrasi": registrasi
                }
            }
        except:
            hasil = []
        return Response({"output": output})


class Detail_Mahasiswa(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['nama']
        pddikti_api = api()
        try:
            detail_mhs = pddikti_api.detail_mahasiswa_by_name(keyword=nama)
            output = {
                "data_umum": {
                    "nm_pd":
                    detail_mhs['dataumum']['nm_pd'],
                    "nipd":
                    detail_mhs['dataumum']['nipd'],
                    "namapt":
                    detail_mhs['dataumum']['namapt'],
                    "namajenjang":
                    detail_mhs['dataumum']['namajenjang'],
                    "namaprodi":
                    detail_mhs['dataumum']['namaprodi'],
                    "jk":
                    detail_mhs['dataumum']['jk'],
                    "reg_pd":
                    detail_mhs['dataumum']['reg_pd'],
                    "mulai_smt":
                    detail_mhs['dataumum']['mulai_smt'],
                    "nm_jns_daftar":
                    detail_mhs['dataumum']['nm_jns_daftar'],
                    "nm_pt_asal":
                    detail_mhs['dataumum']['nm_pt_asal'],
                    "nm_prodi_asal":
                    detail_mhs['dataumum']['nm_prodi_asal'],
                    "ket_keluar":
                    detail_mhs['dataumum']['ket_keluar'],
                    "tgl_keluar":
                    detail_mhs['dataumum']['tgl_keluar'],
                    "no_seri_ijazah":
                    detail_mhs['dataumum']['no_seri_ijazah'],
                    "sert_prof":
                    detail_mhs['dataumum']['sert_prof'],
                    "link_pt":
                    "https://pddikti.kemdikbud.go.id" +
                    detail_mhs['dataumum']['link_pt'],
                    "link_prodi":
                    "https://pddikti.kemdikbud.go.id" +
                    detail_mhs['dataumum']['link_prodi'],
                },
                "statuskuliah": detail_mhs['datastatuskuliah'],
                "data_studi": detail_mhs['datastudi']
            }
        except:
            hasil = []
        return Response({"output": output})


class Detail_Dosen(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['nama_dosen']
        pddikti_api = api()
        detail_dosen = pddikti_api.detail_dosen_by_name(keyword=nama)
        try:
            output = {
                "data_umum": {
                    "id_sdm":
                    detail_dosen['dataumum']['id_sdm'],
                    "nm_sdm":
                    detail_dosen['dataumum']['nm_sdm'],
                    "jk":
                    detail_dosen['dataumum']['jk'],
                    "tmpt_lahir":
                    detail_dosen['dataumum']['tmpt_lahir'],
                    "namapt":
                    detail_dosen['dataumum']['namapt'],
                    "linkpt":
                    "https://pddikti.kemdikbud.go.id" +
                    detail_dosen['dataumum']['linkpt'],
                    "linkprodi":
                    "https://pddikti.kemdikbud.go.id" +
                    detail_dosen['dataumum']['linkprodi'],
                    "namaprodi":
                    detail_dosen['dataumum']['namaprodi'],
                    "statuskeaktifan":
                    detail_dosen['dataumum']['statuskeaktifan'],
                    "pend_tinggi":
                    detail_dosen['dataumum']['pend_tinggi'],
                    "fungsional":
                    detail_dosen['dataumum']['fungsional'],
                    "ikatankerja":
                    detail_dosen['dataumum']['ikatankerja'],
                },
                "data_mengajar": detail_dosen['datamengajar'],
                "data_pendidikan": detail_dosen['datapendidikan']
            }
        except:
            hasil = []
        return Response({"output": output})


class Detail_Univ(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['universitas']
        pddikti_api = api()
        try:
            detail_univ = pddikti_api.detail_data_univ_by_name(keyword=nama)
        except:
            hasil = []
        return Response({"output": detail_univ})


class Detail_Prodi(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['prodi']
        pddikti_api = api()
        try:
            list_prodi = pddikti_api.detail_data_univ_prodi_by_name(
                keyword=nama)
        except:
            hasil = []
        return Response({"output": list_prodi})


class SearchAll(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['nama']
        pddikti_api = api()
        try:
            search_all = pddikti_api.search_all(
                keyword=nama)  #except Mahasiswa
        except:
            hasil = []
        return Response({"output": search_all})


class SearchMahasiswa(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['nama']
        pddikti_api = api()
        search_mhs = pddikti_api.search_mahasiswa(keyword=nama)
        hasil = []
        try:
            for u in search_mhs['mahasiswa']:
                hasil.append({
                    "text":
                    u['text'],
                    "website-link":
                    'https://pddikti.kemdikbud.go.id' + u['website-link']
                })
        except:
            hasil = []
        return Response({"output": hasil})


class SearchProdi(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['prodi']
        pddikti_api = api()
        try:
            search = pddikti_api.search_prodi(keyword=nama)
        except:
            hasil = []
        return Response({"output": search})


class SearchBycategory(APIView
                       ):  #kategori ada 4 Mahasiswa, dosen, pt dan prodi
    def post(self, request):
        data = json.loads(request.body)
        nama = data['nama']
        kat = data['kategori']
        pddikti_api = api()
        try:
            search_kat = pddikti_api.search_by_category(keyword=nama,
                                                        category=kat)
        except:
            hasil = []
        return Response({"output": search_kat})


class SearchDosen(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['nama']
        pddikti_api = api()
        try:
            search_dosen = pddikti_api.search_dosen(keyword=nama)
        except:
            hasil = []
        return Response({"output": search_dosen})


class SearchPt(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['universitas']
        pddikti_api = api()
        try:
            search_pt = pddikti_api.search_pt(keyword=nama)
        except:
            hasil = []
        return Response({"output": search_pt})


class GetAllCampus(APIView):
    def get(self, request):
        pddikti_api = api()
        try:
            data_kampus = pddikti_api.dump_all_univ()
        except:
            hasil = []
        return Response({
            "output": data_kampus,
            "total_kampus": len(data_kampus)
        })


class CountingPT(APIView):
    def post(self, request):
        data = json.loads(request.body)
        nama = data['universitas']
        pddikti_api = api()
        try:
            data_kampus = pddikti_api.detail_univ_jumlah_by_name(keyword=nama)
        except:
            hasil = []
        return Response({"output": data_kampus})

