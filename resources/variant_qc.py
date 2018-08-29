from .basics import *


def get_2_0_2_rf_path(data_type: str, beta: bool):
    """
    Returns path to tab-delimited text files containing 2.0.2 RF results.

    Caveats:
    * Exomes non-beta only contain autosomes
    * Exomes beta only contain release sites

    :param str data_type: One of 'exomes' or 'genomes'
    :param bool beta: When set, returns results of the 'beta' RF using QD and p(AB) rather than the RF using medians
    :return: Path to file
    :rtype: str
    """

    if data_type == 'exomes':
        return 'gs://gnomad/annotations/hail-0.2/ht/exomes/score_rankings/{}'.format('gnomad_exomes.rf.170620_new.txt.bgz' if beta else 'gnomad.exomes.variantqc.txt.bgz')
    else:
        return 'gs://gnomad/annotations/hail-0.2/ht/genomes/score_rankings/{}'.format('rf_as_qd_max_pab.rf.txt.bgz' if beta else 'gnomad.sites.RF.newStats24.txt.bgz')


def rf_run_hash_path(data_type: str, hail_version: str = CURRENT_HAIL_VERSION):
    """
    Returns the path to the json file containing the RF runs list.

    :param str data_type: One of 'exomes' or 'genomes'
    :param str hail_version: One of the HAIL_VERSIONs
    :return: Path to json file
    :rtype: str
    """

    return 'gs://gnomad/annotations/hail-{0}/mt/{1}/rf/gnomad.{1}.runs.json'.format(hail_version, data_type)


def rf_annotated_path(
        data_type: str,
        adj: bool = False,
        hail_version: str = CURRENT_HAIL_VERSION
) -> str:
    """
    Returns the path to the RF-ready annotated HT

    :param str data_type: One of 'exomes' or 'genomes'
    :param bool adj: Whether to load 'adj' or 'raw'
    :param hail_version: One of the HAIL_VERSIONs
    :return:
    """
    return 'gs://gnomad/annotations/hail-{0}/mt/{1}/rf/gnomad.{1}.{2}.ht'.format(
        hail_version,
        data_type,
        "adj" if adj else 'raw')


def rf_path(data_type: str,
            data: str = 'rf_result',
            run_hash: str = None,
            hail_version: str = CURRENT_HAIL_VERSION
            ) -> str:
    """

    Gets the path to the desired RF data.
    Data can take the following values:
        - 'training': path to the training data for a given run
        - 'model': path to pyspark pipeline RF model
        - 'rf_result' (default): path to HT containing result of RF filtering

    :param str data_type: One of 'exomes' or 'genomes'
    :param str data: One of 'pre_rf', 'training', 'model' or 'rf_result' (default)
    :param str run_hash: Hash of RF run to load
    :param str hail_version: One of the HAIL_VERSIONs
    :return:
    """

    extension = 'model' if data == 'model' else 'ht'
    return 'gs://gnomad/annotations/hail-{0}/mt/{1}/rf/{2}/gnomad.{1}.{2}.{3}.{4}'.format(hail_version, data_type, run_hash, data, extension)


def score_ranking_path(data_type: str,
            data: str,
            binned: bool = False,
            hail_version: str = CURRENT_HAIL_VERSION
            ) -> str:
    """
    Returns the path to non-RF metrics score rankings Tables, e.g.:
    * vqsr
    * cnn
    * rf_2.0.2
    * rf_2.0.2_beta

    :param data_type: One of 'exomes' or 'genomes'
    :param data: The score data to return
    :param binned: Whether to get the binned data
    :param hail_version: Hail version
    :return: Path to desired hail Table
    :rtype: str
    """

    return 'gs://gnomad/annotations/hail-{0}/ht/{1}/score_rankings/gnomad.{1}.{2}{3}.ht'.format(hail_version,
                                                                                                data_type,
                                                                                                data,
                                                                                                '_binned' if binned else '')


def validated_denovos_path():
    return 'gs://gnomad/resources/validated_de_novos.txt.bgz'

