from pmd5_ok.request import dec_pmd5
from ttmd5_ok.request import dec_ttmd5
from t007_ok.request import dec_t007

if __name__ == "__main__":
    md5_str = "e10adc3949ba59abbe56e057f20f883e"
    dec_ttmd5(md5_str)
    dec_pmd5(md5_str)
    dec_t007(md5_str)








