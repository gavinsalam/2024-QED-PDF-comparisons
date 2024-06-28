Q=100
for pdf in NNPDF31_nnlo_as_0118_luxqed MSHT20qed_nnlo NNPDF31_nnlo_as_0118 MSHT20nnlo_as118 NNPDF40_nnlo_as_01180_qed NNPDF40_nnlo_as_01180
do
    echo doing $pdf
    pdf.py -Q $Q -flav=22,-5,-4,-3,-2,-1,21,1,2,3,4,5 -pdf $pdf -out pdf-files/$pdf-Q$Q.dat
done