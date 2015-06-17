from mvpa2.clfs.svm import LinearCSVMC
from mvpa2.generators.partition import NFoldPartitioner
from mvpa2.measures.base import CrossValidation
from mvpa2.misc.errorfx import mean_match_accuracy
from mvpa2.mappers.fx import mean_sample

clf = LinearCSVMC(space='condition')
obj = CrossValidation(
        clf,
        NFoldPartitioner(),
        errorfx=mean_match_accuracy,
        postproc=mean_sample(),
        enable_ca=['stats'])
