#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-matrixStats
Version  : 0.53.1
Release  : 9
URL      : https://cran.r-project.org/src/contrib/matrixStats_0.53.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/matrixStats_0.53.1.tar.gz
Summary  : Functions that Apply to Rows and Columns of Matrices (and to
Group    : Development/Tools
License  : Artistic-2.0
Requires: R-matrixStats-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-matrixStats package.
Group: Libraries

%description lib
lib components for the R-matrixStats package.


%prep
%setup -q -c -n matrixStats

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523317372

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523317372
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library matrixStats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library matrixStats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library matrixStats
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library matrixStats|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/matrixStats/DESCRIPTION
/usr/lib64/R/library/matrixStats/INDEX
/usr/lib64/R/library/matrixStats/Meta/Rd.rds
/usr/lib64/R/library/matrixStats/Meta/features.rds
/usr/lib64/R/library/matrixStats/Meta/hsearch.rds
/usr/lib64/R/library/matrixStats/Meta/links.rds
/usr/lib64/R/library/matrixStats/Meta/nsInfo.rds
/usr/lib64/R/library/matrixStats/Meta/package.rds
/usr/lib64/R/library/matrixStats/Meta/vignette.rds
/usr/lib64/R/library/matrixStats/NAMESPACE
/usr/lib64/R/library/matrixStats/NEWS
/usr/lib64/R/library/matrixStats/R/matrixStats
/usr/lib64/R/library/matrixStats/R/matrixStats.rdb
/usr/lib64/R/library/matrixStats/R/matrixStats.rdx
/usr/lib64/R/library/matrixStats/benchmarking/R/random-matrices.R
/usr/lib64/R/library/matrixStats/benchmarking/R/random-vectors.R
/usr/lib64/R/library/matrixStats/benchmarking/allocMatrix.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/allocVector.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/anyMissing.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/anyMissing_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/binCounts.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/binCounts_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/binMeans.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/binMeans_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowAlls.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowAlls_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowAnyMissings.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowAnyMissings_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowAnys.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowAnys_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCounts.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCounts_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCummins.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCummins_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCumprods.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCumprods_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCumsums.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowCumsums_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowDiffs.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowDiffs_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowLogSumExps.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowLogSumExps_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMads.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMads_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMeans2.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMeans2_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMedians.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMedians_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMins.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowMins_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowOrderStats.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowOrderStats_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowProds.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowProds_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowQuantiles.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowQuantiles_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowRanges.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowRanges_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowRanks.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowRanks_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowSums2.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowSums2_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowTabulates.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowTabulates_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowVars.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowVars_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowWeightedMeans.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowWeightedMeans_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowWeightedMedians.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/colRowWeightedMedians_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/count.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/count_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/includes/appendix.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/includes/footer.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/includes/header.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/includes/references.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/includes/results.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/includes/setup.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/index.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/indexByRow.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/logSumExp.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/logSumExp_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/madDiff.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/madDiff_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/mean2.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/mean2_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/product.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/product_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/sum2.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/sum2_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/t_tx_OP_y.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/t_tx_OP_y_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/varDiff.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/varDiff_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/weightedMean.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/weightedMean_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/weightedMedian.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/weightedMedian_subset.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/x_OP_y.md.rsp
/usr/lib64/R/library/matrixStats/benchmarking/x_OP_y_subset.md.rsp
/usr/lib64/R/library/matrixStats/doc/index.html
/usr/lib64/R/library/matrixStats/doc/matrixStats-methods.html
/usr/lib64/R/library/matrixStats/doc/matrixStats-methods.md.rsp
/usr/lib64/R/library/matrixStats/help/AnIndex
/usr/lib64/R/library/matrixStats/help/aliases.rds
/usr/lib64/R/library/matrixStats/help/matrixStats.rdb
/usr/lib64/R/library/matrixStats/help/matrixStats.rdx
/usr/lib64/R/library/matrixStats/help/paths.rds
/usr/lib64/R/library/matrixStats/html/00Index.html
/usr/lib64/R/library/matrixStats/html/R.css
/usr/lib64/R/library/matrixStats/tests/allocArray.R
/usr/lib64/R/library/matrixStats/tests/allocMatrix.R
/usr/lib64/R/library/matrixStats/tests/allocVector.R
/usr/lib64/R/library/matrixStats/tests/anyMissing.R
/usr/lib64/R/library/matrixStats/tests/anyMissing_subset.R
/usr/lib64/R/library/matrixStats/tests/benchmark.R
/usr/lib64/R/library/matrixStats/tests/binCounts.R
/usr/lib64/R/library/matrixStats/tests/binCounts_subset.R
/usr/lib64/R/library/matrixStats/tests/binMeans,binCounts.R
/usr/lib64/R/library/matrixStats/tests/binMeans,binCounts_subset.R
/usr/lib64/R/library/matrixStats/tests/count.R
/usr/lib64/R/library/matrixStats/tests/count_subset.R
/usr/lib64/R/library/matrixStats/tests/diff2.R
/usr/lib64/R/library/matrixStats/tests/diff2_subset.R
/usr/lib64/R/library/matrixStats/tests/indexByRow.R
/usr/lib64/R/library/matrixStats/tests/logSumExp.R
/usr/lib64/R/library/matrixStats/tests/logSumExp_subset.R
/usr/lib64/R/library/matrixStats/tests/mean2.R
/usr/lib64/R/library/matrixStats/tests/mean2_subset.R
/usr/lib64/R/library/matrixStats/tests/product.R
/usr/lib64/R/library/matrixStats/tests/product_subset.R
/usr/lib64/R/library/matrixStats/tests/psortKM.R
/usr/lib64/R/library/matrixStats/tests/rowAllAnys.R
/usr/lib64/R/library/matrixStats/tests/rowAllAnys_subset.R
/usr/lib64/R/library/matrixStats/tests/rowAvgsPerColSet.R
/usr/lib64/R/library/matrixStats/tests/rowAvgsPerColSet_subset.R
/usr/lib64/R/library/matrixStats/tests/rowCollapse.R
/usr/lib64/R/library/matrixStats/tests/rowCollapse_subset.R
/usr/lib64/R/library/matrixStats/tests/rowCounts.R
/usr/lib64/R/library/matrixStats/tests/rowCounts_subset.R
/usr/lib64/R/library/matrixStats/tests/rowCumMinMaxs.R
/usr/lib64/R/library/matrixStats/tests/rowCumMinMaxs_subset.R
/usr/lib64/R/library/matrixStats/tests/rowCumprods.R
/usr/lib64/R/library/matrixStats/tests/rowCumprods_subset.R
/usr/lib64/R/library/matrixStats/tests/rowCumsums.R
/usr/lib64/R/library/matrixStats/tests/rowCumsums_subset.R
/usr/lib64/R/library/matrixStats/tests/rowDiffs.R
/usr/lib64/R/library/matrixStats/tests/rowDiffs_subset.R
/usr/lib64/R/library/matrixStats/tests/rowIQRs.R
/usr/lib64/R/library/matrixStats/tests/rowIQRs_subset.R
/usr/lib64/R/library/matrixStats/tests/rowLogSumExps.R
/usr/lib64/R/library/matrixStats/tests/rowLogSumExps_subset.R
/usr/lib64/R/library/matrixStats/tests/rowMads.R
/usr/lib64/R/library/matrixStats/tests/rowMads_subset.R
/usr/lib64/R/library/matrixStats/tests/rowMeans2.R
/usr/lib64/R/library/matrixStats/tests/rowMeans2_subset.R
/usr/lib64/R/library/matrixStats/tests/rowMedians.R
/usr/lib64/R/library/matrixStats/tests/rowMedians_subset.R
/usr/lib64/R/library/matrixStats/tests/rowOrderStats.R
/usr/lib64/R/library/matrixStats/tests/rowOrderStats_subset.R
/usr/lib64/R/library/matrixStats/tests/rowProds.R
/usr/lib64/R/library/matrixStats/tests/rowProds_subset.R
/usr/lib64/R/library/matrixStats/tests/rowQuantiles.R
/usr/lib64/R/library/matrixStats/tests/rowQuantiles_subset.R
/usr/lib64/R/library/matrixStats/tests/rowRanges.R
/usr/lib64/R/library/matrixStats/tests/rowRanges_subset.R
/usr/lib64/R/library/matrixStats/tests/rowRanks.R
/usr/lib64/R/library/matrixStats/tests/rowRanks_subset.R
/usr/lib64/R/library/matrixStats/tests/rowSds.R
/usr/lib64/R/library/matrixStats/tests/rowSds_subset.R
/usr/lib64/R/library/matrixStats/tests/rowSums2.R
/usr/lib64/R/library/matrixStats/tests/rowSums2_subset.R
/usr/lib64/R/library/matrixStats/tests/rowTabulates.R
/usr/lib64/R/library/matrixStats/tests/rowTabulates_subset.R
/usr/lib64/R/library/matrixStats/tests/rowVarDiffs.R
/usr/lib64/R/library/matrixStats/tests/rowVarDiffs_mad,iqr_subset.R
/usr/lib64/R/library/matrixStats/tests/rowVarDiffs_var,sd_subset.R
/usr/lib64/R/library/matrixStats/tests/rowVars.R
/usr/lib64/R/library/matrixStats/tests/rowVars_subset.R
/usr/lib64/R/library/matrixStats/tests/rowWeightedMeans.R
/usr/lib64/R/library/matrixStats/tests/rowWeightedMeans_subset.R
/usr/lib64/R/library/matrixStats/tests/rowWeightedMedians.R
/usr/lib64/R/library/matrixStats/tests/rowWeightedMedians_subset.R
/usr/lib64/R/library/matrixStats/tests/rowWeightedVars.R
/usr/lib64/R/library/matrixStats/tests/rowWeightedVars_subset.R
/usr/lib64/R/library/matrixStats/tests/signTabulate.R
/usr/lib64/R/library/matrixStats/tests/signTabulate_subset.R
/usr/lib64/R/library/matrixStats/tests/sum2.R
/usr/lib64/R/library/matrixStats/tests/sum2_subset.R
/usr/lib64/R/library/matrixStats/tests/utils/validateIndicesFramework.R
/usr/lib64/R/library/matrixStats/tests/validateIndices.R
/usr/lib64/R/library/matrixStats/tests/varDiff_etal.R
/usr/lib64/R/library/matrixStats/tests/varDiff_etal_subset.R
/usr/lib64/R/library/matrixStats/tests/weightedMean.R
/usr/lib64/R/library/matrixStats/tests/weightedMean_subset.R
/usr/lib64/R/library/matrixStats/tests/weightedMedian.R
/usr/lib64/R/library/matrixStats/tests/weightedMedian_subset.R
/usr/lib64/R/library/matrixStats/tests/weightedVar.R
/usr/lib64/R/library/matrixStats/tests/weightedVar_etal.R
/usr/lib64/R/library/matrixStats/tests/weightedVar_etal_subset.R
/usr/lib64/R/library/matrixStats/tests/x_OP_y.R
/usr/lib64/R/library/matrixStats/tests/x_OP_y_subset.R
/usr/lib64/R/library/matrixStats/tests/zzz.package-unload.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/matrixStats/libs/matrixStats.so
/usr/lib64/R/library/matrixStats/libs/matrixStats.so.avx2
/usr/lib64/R/library/matrixStats/libs/matrixStats.so.avx512
