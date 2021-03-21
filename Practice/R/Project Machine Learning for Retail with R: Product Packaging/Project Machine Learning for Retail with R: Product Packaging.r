#[Petunjuk Penyelesaian Project](https://academy.dqlab.id/main/livecode/16/109/516)
library(arules)
transaksi_tabular <- read.transactions(file='https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv', 
                                       format="single", sep="\t", cols=c(1,2), skip=1)
write(transaksi_tabular, file="test_project_retail_1.txt", sep=",")

#[Output Awal: Statistik Top 10](https://academy.dqlab.id/main/livecode/16/109/517)
library(arules)
transaksi_tabular<-read.transactions(file="transaksi_dqlab_retail.tsv", format="single", sep="\t", cols=c(1,2), skip=1)
data_item<-itemFrequency(transaksi_tabular, type="absolut")
data_item<-sort(data_item, decreasing=TRUE)
data_item<-data_item[1:10]
data_item<-data.frame("Nama Produk"=names(data_item),"Jumlah"=data_item, row.names=NULL)
inspect(data_item)
write.csv(data_item, file="top10_item_retail.txt", sep=",")

#[Output Awal: Statistik Bottom 10](https://academy.dqlab.id/main/livecode/16/109/518)
library(arules)
transaksi_tabular<-read.transactions(file="https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv", format="single", sep="\t", cols=c(1,2), skip=1)
data_item<-itemFrequency(transaksi_tabular, type="absolut")
data_item<-sort(data_item, decreasing=FALSE)
data_item<-data_item[1:10]
data_item<-data.frame("Nama Produk"=names(data_item),"Jumlah"=data_item, row.names=NULL)
inspect(data_item)
write.csv(data_item, file="bottom10_item_retail.txt", sep=",")

#[Mendapatkan Kombinasi Produk yang menarik](https://academy.dqlab.id/main/livecode/16/109/519)
library(arules)
transaksi_tabular<-read.transactions(file="https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv", format="single", sep="\t", cols=c(1,2), skip=1)
mba<-apriori(transaksi_tabular, parameter=list(support=10/length(transaksi_tabular), confidence=0.5, minlen=2, maxlen=3))
mba<-head(sort(mba, by="lift", decreasing=T), n=10)
inspect(mba)
write(mba, file="kombinasi_retail.txt")

#[Mencari Paket Produk yang bisa dipasangkan dengan Item Slow-Moving](https://academy.dqlab.id/main/livecode/16/109/520)
library(arules)
transaksi_tabular <- read.transactions(file="transaksi_dqlab_retail.tsv", format="single", sep="\t", cols=c(1,2), skip=1)
jumlah_transaksi<-length(transaksi_tabular)
jumlah_kemunculan_minimal <- 10
mba <- apriori(transaksi_tabular,parameter= list(supp=jumlah_kemunculan_minimal/jumlah_transaksi,
              conf=0.1, minlen=2, maxlen=3))
mba1 <- subset(mba, lift > 1 & rhs %in% "Tas Makeup")
mba1 <- sort(mba1, by='lift', decreasing = T)[1:3]
mba2 <- subset(mba, lift > 1 & rhs %in% "Baju Renang Pria Anak-anak")
mba2 <- sort(mba2, by='lift', decreasing = T)[1:3]
mba <- c(mba1, mba2)
inspect(mba)
write(mba,file="kombinasi_retail_slow_moving.txt")
