export PYTHONPATH="${PWD}/..:${PWD}/../..:"

THREADS=30

# Disable multithreading in all numerical packages
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1

python3 \
    ./pipelines/process_yelp_reviews.py \
    --threads=${THREADS} \
    $1
