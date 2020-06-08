from django.db import models
from django_pandas.managers import DataFrameManager


# Create your models here.
class Promoters154CellsBinarized(models.Model):
    index = models.TextField(blank=True, primary_key=True)  # Auto-generated had: , null=True
    adipocyte_breast = models.BigIntegerField(db_column='Adipocyte - breast', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipocyte_omental = models.BigIntegerField(db_column='Adipocyte - omental', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipocyte_perirenal = models.BigIntegerField(db_column='Adipocyte - perirenal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipocyte_subcutaneous = models.BigIntegerField(db_column='Adipocyte - subcutaneous', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alveolar_epithelial_cells = models.BigIntegerField(db_column='Alveolar Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amniotic_epithelial_cells = models.BigIntegerField(db_column='Amniotic Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amniotic_membrane_cells = models.BigIntegerField(db_column='amniotic membrane cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    anulus_pulposus_cell = models.BigIntegerField(db_column='Anulus Pulposus Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    astrocyte_cerebellum = models.BigIntegerField(db_column='Astrocyte - cerebellum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    astrocyte_cerebral_cortex = models.BigIntegerField(db_column='Astrocyte - cerebral cortex', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    basophils = models.BigIntegerField(db_column='Basophils', blank=True, null=True)  # Field name made lowercase.
    bronchial_epithelial_cell = models.BigIntegerField(db_column='Bronchial Epithelial Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cardiac_myocyte = models.BigIntegerField(db_column='Cardiac Myocyte', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd133_stem_cells_adult_bone_marrow_derived = models.BigIntegerField(db_column='CD133+ stem cells - adult bone marrow derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd133_stem_cells_cord_blood_derived = models.BigIntegerField(db_column='CD133+ stem cells - cord blood derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_monocyte_derived_endothelial_progenitor_cells = models.BigIntegerField(db_column='CD14+ monocyte derived endothelial progenitor cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_monocytes = models.BigIntegerField(db_column='CD14+ Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_cd16_monocytes = models.BigIntegerField(db_column='CD14+ CD16- Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_cd16_monocytes_0 = models.BigIntegerField(db_column='CD14+ CD16+ Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    cd14_cd16_monocytes_1 = models.BigIntegerField(db_column='CD14- CD16+ Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    cd19_b_cells = models.BigIntegerField(db_column='CD19+ B Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd34_cells_differentiated_to_erythrocyte_lineage = models.BigIntegerField(db_column='CD34 cells differentiated to erythrocyte lineage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd34_progenitors = models.BigIntegerField(db_column='CD34+ Progenitors', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd34_stem_cells_adult_bone_marrow_derived = models.BigIntegerField(db_column='CD34+ stem cells - adult bone marrow derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_t_cells = models.BigIntegerField(db_column='CD4+ T Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_memory_regulatory_t_cells = models.BigIntegerField(db_column='CD4+CD25+CD45RA- memory regulatory T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_naive_regulatory_t_cells = models.BigIntegerField(db_column='CD4+CD25+CD45RA+ naive regulatory T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_memory_conventional_t_cells = models.BigIntegerField(db_column='CD4+CD25-CD45RA- memory conventional T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_naive_conventional_t_cells = models.BigIntegerField(db_column='CD4+CD25-CD45RA+ naive conventional T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd8_t_cells = models.BigIntegerField(db_column='CD8+ T Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chondrocyte = models.BigIntegerField(db_column='Chondrocyte', blank=True, null=True)  # Field name made lowercase.
    chorionic_membrane_cells = models.BigIntegerField(db_column='chorionic membrane cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ciliary_epithelial_cells = models.BigIntegerField(db_column='Ciliary Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    common_myeloid_progenitor_cmp = models.BigIntegerField(db_column='common myeloid progenitor CMP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    corneal_epithelial_cells = models.BigIntegerField(db_column='Corneal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dendritic_cells_monocyte_immature_derived = models.BigIntegerField(db_column='Dendritic Cells - monocyte immature derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dendritic_cells_plasmacytoid = models.BigIntegerField(db_column='Dendritic Cells - plasmacytoid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_aortic = models.BigIntegerField(db_column='Endothelial Cells - Aortic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_artery = models.BigIntegerField(db_column='Endothelial Cells - Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_lymphatic = models.BigIntegerField(db_column='Endothelial Cells - Lymphatic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_microvascular = models.BigIntegerField(db_column='Endothelial Cells - Microvascular', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_thoracic = models.BigIntegerField(db_column='Endothelial Cells - Thoracic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_umbilical_vein = models.BigIntegerField(db_column='Endothelial Cells - Umbilical vein', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_vein = models.BigIntegerField(db_column='Endothelial Cells - Vein', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eosinophils = models.BigIntegerField(db_column='Eosinophils', blank=True, null=True)  # Field name made lowercase.
    esophageal_epithelial_cells = models.BigIntegerField(db_column='Esophageal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_aortic_adventitial = models.BigIntegerField(db_column='Fibroblast - Aortic Adventitial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_cardiac = models.BigIntegerField(db_column='Fibroblast - Cardiac', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_choroid_plexus = models.BigIntegerField(db_column='Fibroblast - Choroid Plexus', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_conjunctival = models.BigIntegerField(db_column='Fibroblast - Conjunctival', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_dermal = models.BigIntegerField(db_column='Fibroblast - Dermal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_gingival = models.BigIntegerField(db_column='Fibroblast - Gingival', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_lung = models.BigIntegerField(db_column='Fibroblast - Lung', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_lymphatic = models.BigIntegerField(db_column='Fibroblast - Lymphatic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_mammary = models.BigIntegerField(db_column='Fibroblast - Mammary', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_periodontal_ligament = models.BigIntegerField(db_column='Fibroblast - Periodontal Ligament', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_pulmonary_artery = models.BigIntegerField(db_column='Fibroblast - Pulmonary Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_skin = models.BigIntegerField(db_column='Fibroblast - skin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_villous_mesenchymal = models.BigIntegerField(db_column='Fibroblast - Villous Mesenchymal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gamma_delta_positive_t_cells = models.BigIntegerField(db_column='gamma delta positive T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gingival_epithelial_cells = models.BigIntegerField(db_column='Gingival epithelial cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    granulocyte_macrophage_progenitor = models.BigIntegerField(db_column='granulocyte macrophage progenitor', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hair_follicle_dermal_papilla_cells = models.BigIntegerField(db_column='Hair Follicle Dermal Papilla Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hair_follicle_outer_root_sheath_cells = models.BigIntegerField(db_column='Hair Follicle Outer Root Sheath Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hepatic_sinusoidal_endothelial_cells = models.BigIntegerField(db_column='Hepatic Sinusoidal Endothelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hepatic_stellate_cells_lipocyte_field = models.BigIntegerField(db_column='Hepatic Stellate Cells (lipocyte)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hepatocyte = models.BigIntegerField(db_column='Hepatocyte', blank=True, null=True)  # Field name made lowercase.
    immature_langerhans_cells = models.BigIntegerField(db_column='immature langerhans cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    intestinal_epithelial_cells_polarized_field = models.BigIntegerField(db_column='Intestinal epithelial cells (polarized)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    iris_pigment_epithelial_cells = models.BigIntegerField(db_column='Iris Pigment Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keratinocyte_epidermal = models.BigIntegerField(db_column='Keratinocyte - epidermal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keratinocyte_oral = models.BigIntegerField(db_column='Keratinocyte - oral', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keratocytes = models.BigIntegerField(db_column='Keratocytes', blank=True, null=True)  # Field name made lowercase.
    lens_epithelial_cells = models.BigIntegerField(db_column='Lens Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    macrophage_monocyte_derived = models.BigIntegerField(db_column='Macrophage - monocyte derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mallassez_derived_cells = models.BigIntegerField(db_column='Mallassez-derived cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mammary_epithelial_cell = models.BigIntegerField(db_column='Mammary Epithelial Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mast_cell = models.BigIntegerField(db_column='Mast cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mature_adipocyte = models.BigIntegerField(db_column='mature adipocyte', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melanocyte = models.BigIntegerField(db_column='Melanocyte', blank=True, null=True)  # Field name made lowercase.
    meningeal_cells = models.BigIntegerField(db_column='Meningeal Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_precursor_cell_adipose = models.BigIntegerField(db_column='mesenchymal precursor cell - adipose', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mesenchymal_precursor_cell_bone_marrow = models.BigIntegerField(db_column='mesenchymal precursor cell - bone marrow', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mesenchymal_precursor_cell_cardiac = models.BigIntegerField(db_column='mesenchymal precursor cell - cardiac', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_adipose = models.BigIntegerField(db_column='Mesenchymal stem cells - adipose', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_amniotic_membrane = models.BigIntegerField(db_column='Mesenchymal Stem Cells - amniotic membrane', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_bone_marrow = models.BigIntegerField(db_column='Mesenchymal Stem Cells - bone marrow', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_hepatic = models.BigIntegerField(db_column='Mesenchymal stem cells - hepatic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_umbilical = models.BigIntegerField(db_column='Mesenchymal stem cells - umbilical', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_vertebral = models.BigIntegerField(db_column='Mesenchymal Stem Cells - Vertebral', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_wharton_jelly = models.BigIntegerField(db_column='Mesenchymal Stem Cells - Wharton Jelly', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesothelial_cells = models.BigIntegerField(db_column='Mesothelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    migratory_langerhans_cells = models.BigIntegerField(db_column='migratory langerhans cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    multipotent_cord_blood_unrestricted_somatic_stem_cells = models.BigIntegerField(db_column='Multipotent Cord Blood Unrestricted Somatic Stem Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    myoblast = models.BigIntegerField(db_column='Myoblast', blank=True, null=True)  # Field name made lowercase.
    nasal_epithelial_cells = models.BigIntegerField(db_column='nasal epithelial cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    natural_killer_cells = models.BigIntegerField(db_column='Natural Killer Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    neural_stem_cells = models.BigIntegerField(db_column='Neural stem cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    neurons = models.BigIntegerField(db_column='Neurons', blank=True, null=True)  # Field name made lowercase.
    neutrophil = models.BigIntegerField(db_column='Neutrophil', blank=True, null=True)  # Field name made lowercase.
    nucleus_pulposus_cell = models.BigIntegerField(db_column='Nucleus Pulposus Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    olfactory_epithelial_cells = models.BigIntegerField(db_column='Olfactory epithelial cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oligodendrocyte_precursors = models.BigIntegerField(db_column='Oligodendrocyte - precursors', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    osteoblast = models.BigIntegerField(db_column='Osteoblast', blank=True, null=True)  # Field name made lowercase.
    pancreatic_stromal_cells = models.BigIntegerField(db_column='Pancreatic stromal cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pericytes = models.BigIntegerField(db_column='Pericytes', blank=True, null=True)  # Field name made lowercase.
    perineurial_cells = models.BigIntegerField(db_column='Perineurial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    placental_epithelial_cells = models.BigIntegerField(db_column='Placental Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_breast = models.BigIntegerField(db_column='Preadipocyte - breast', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_omental = models.BigIntegerField(db_column='Preadipocyte - omental', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_perirenal = models.BigIntegerField(db_column='Preadipocyte - perirenal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_subcutaneous = models.BigIntegerField(db_column='Preadipocyte - subcutaneous', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_visceral = models.BigIntegerField(db_column='Preadipocyte - visceral', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    promyelocytes = models.BigIntegerField(blank=True, null=True)
    prostate_epithelial_cells = models.BigIntegerField(db_column='Prostate Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prostate_stromal_cells = models.BigIntegerField(db_column='Prostate Stromal Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_cortical_epithelial_cells = models.BigIntegerField(db_column='Renal Cortical Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_epithelial_cells = models.BigIntegerField(db_column='Renal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_glomerular_endothelial_cells = models.BigIntegerField(db_column='Renal Glomerular Endothelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_mesangial_cells = models.BigIntegerField(db_column='Renal Mesangial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_proximal_tubular_epithelial_cell = models.BigIntegerField(db_column='Renal Proximal Tubular Epithelial Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retinal_pigment_epithelial_cells = models.BigIntegerField(db_column='Retinal Pigment Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salivary_acinar_cells = models.BigIntegerField(db_column='salivary acinar cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    schwann_cells = models.BigIntegerField(db_column='Schwann Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sebocyte = models.BigIntegerField(db_column='Sebocyte', blank=True, null=True)  # Field name made lowercase.
    sertoli_cells = models.BigIntegerField(db_column='Sertoli Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skeletal_muscle_cells = models.BigIntegerField(db_column='Skeletal Muscle Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skeletal_muscle_cells_differentiated_into_myotubes = models.BigIntegerField(db_column='Skeletal muscle cells differentiated into Myotubes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skeletal_muscle_satellite_cells = models.BigIntegerField(db_column='Skeletal Muscle Satellite Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    small_airway_epithelial_cells = models.BigIntegerField(db_column='Small Airway Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_airway = models.BigIntegerField(db_column='Smooth muscle cells - airway', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_aortic = models.BigIntegerField(db_column='Smooth Muscle Cells - Aortic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_bladder = models.BigIntegerField(db_column='Smooth Muscle Cells - Bladder', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_brachiocephalic = models.BigIntegerField(db_column='Smooth Muscle Cells - Brachiocephalic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_brain_vascular = models.BigIntegerField(db_column='Smooth Muscle Cells - Brain Vascular', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_bronchial = models.BigIntegerField(db_column='Smooth Muscle Cells - Bronchial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_carotid = models.BigIntegerField(db_column='Smooth Muscle Cells - Carotid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_colonic = models.BigIntegerField(db_column='Smooth Muscle Cells - Colonic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_coronary_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Coronary Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_esophageal = models.BigIntegerField(db_column='Smooth Muscle Cells - Esophageal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_internal_thoracic_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Internal Thoracic Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_intestinal = models.BigIntegerField(db_column='Smooth Muscle Cells - Intestinal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_prostate = models.BigIntegerField(db_column='Smooth Muscle Cells - Prostate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_pulmonary_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Pulmonary Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_subclavian_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Subclavian Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_tracheal = models.BigIntegerField(db_column='Smooth Muscle Cells - Tracheal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_umbilical_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Umbilical artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_umbilical_vein = models.BigIntegerField(db_column='Smooth Muscle Cells - Umbilical Vein', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_uterine = models.BigIntegerField(db_column='Smooth Muscle Cells - Uterine', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    synoviocyte = models.BigIntegerField(db_column='Synoviocyte', blank=True, null=True)  # Field name made lowercase.
    tenocyte = models.BigIntegerField(blank=True, null=True)
    trabecular_meshwork_cells = models.BigIntegerField(db_column='Trabecular Meshwork Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tracheal_epithelial_cells = models.BigIntegerField(db_column='Tracheal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urothelial_cells = models.BigIntegerField(db_column='Urothelial cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    objects = models.Manager()
    pdobjects = DataFrameManager()  # Pandas-Enabled Manager

    class Meta:
        managed = False
        db_table = 'promoters_154cells_binarized'


class Enhancers154CellsBinarized(models.Model):
    index = models.TextField(blank=True, primary_key=True)  # Auto-generated had: , null=True
    adipocyte_breast = models.BigIntegerField(db_column='Adipocyte - breast', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipocyte_omental = models.BigIntegerField(db_column='Adipocyte - omental', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipocyte_perirenal = models.BigIntegerField(db_column='Adipocyte - perirenal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adipocyte_subcutaneous = models.BigIntegerField(db_column='Adipocyte - subcutaneous', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alveolar_epithelial_cells = models.BigIntegerField(db_column='Alveolar Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amniotic_epithelial_cells = models.BigIntegerField(db_column='Amniotic Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amniotic_membrane_cells = models.BigIntegerField(db_column='amniotic membrane cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    anulus_pulposus_cell = models.BigIntegerField(db_column='Anulus Pulposus Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    astrocyte_cerebellum = models.BigIntegerField(db_column='Astrocyte - cerebellum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    astrocyte_cerebral_cortex = models.BigIntegerField(db_column='Astrocyte - cerebral cortex', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    basophils = models.BigIntegerField(db_column='Basophils', blank=True, null=True)  # Field name made lowercase.
    bronchial_epithelial_cell = models.BigIntegerField(db_column='Bronchial Epithelial Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cardiac_myocyte = models.BigIntegerField(db_column='Cardiac Myocyte', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd133_stem_cells_adult_bone_marrow_derived = models.BigIntegerField(db_column='CD133+ stem cells - adult bone marrow derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd133_stem_cells_cord_blood_derived = models.BigIntegerField(db_column='CD133+ stem cells - cord blood derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_monocyte_derived_endothelial_progenitor_cells = models.BigIntegerField(db_column='CD14+ monocyte derived endothelial progenitor cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_monocytes = models.BigIntegerField(db_column='CD14+ Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_cd16_monocytes = models.BigIntegerField(db_column='CD14+ CD16- Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd14_cd16_monocytes_0 = models.BigIntegerField(db_column='CD14+ CD16+ Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    cd14_cd16_monocytes_1 = models.BigIntegerField(db_column='CD14- CD16+ Monocytes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    cd19_b_cells = models.BigIntegerField(db_column='CD19+ B Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd34_cells_differentiated_to_erythrocyte_lineage = models.BigIntegerField(db_column='CD34 cells differentiated to erythrocyte lineage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd34_progenitors = models.BigIntegerField(db_column='CD34+ Progenitors', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd34_stem_cells_adult_bone_marrow_derived = models.BigIntegerField(db_column='CD34+ stem cells - adult bone marrow derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_t_cells = models.BigIntegerField(db_column='CD4+ T Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_memory_regulatory_t_cells = models.BigIntegerField(db_column='CD4+CD25+CD45RA- memory regulatory T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_naive_regulatory_t_cells = models.BigIntegerField(db_column='CD4+CD25+CD45RA+ naive regulatory T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_memory_conventional_t_cells = models.BigIntegerField(db_column='CD4+CD25-CD45RA- memory conventional T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd4_cd25_cd45ra_naive_conventional_t_cells = models.BigIntegerField(db_column='CD4+CD25-CD45RA+ naive conventional T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cd8_t_cells = models.BigIntegerField(db_column='CD8+ T Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chondrocyte = models.BigIntegerField(db_column='Chondrocyte', blank=True, null=True)  # Field name made lowercase.
    chorionic_membrane_cells = models.BigIntegerField(db_column='chorionic membrane cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ciliary_epithelial_cells = models.BigIntegerField(db_column='Ciliary Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    common_myeloid_progenitor_cmp = models.BigIntegerField(db_column='common myeloid progenitor CMP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    corneal_epithelial_cells = models.BigIntegerField(db_column='Corneal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dendritic_cells_monocyte_immature_derived = models.BigIntegerField(db_column='Dendritic Cells - monocyte immature derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dendritic_cells_plasmacytoid = models.BigIntegerField(db_column='Dendritic Cells - plasmacytoid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_aortic = models.BigIntegerField(db_column='Endothelial Cells - Aortic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_artery = models.BigIntegerField(db_column='Endothelial Cells - Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_lymphatic = models.BigIntegerField(db_column='Endothelial Cells - Lymphatic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_microvascular = models.BigIntegerField(db_column='Endothelial Cells - Microvascular', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_thoracic = models.BigIntegerField(db_column='Endothelial Cells - Thoracic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_umbilical_vein = models.BigIntegerField(db_column='Endothelial Cells - Umbilical vein', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    endothelial_cells_vein = models.BigIntegerField(db_column='Endothelial Cells - Vein', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eosinophils = models.BigIntegerField(db_column='Eosinophils', blank=True, null=True)  # Field name made lowercase.
    esophageal_epithelial_cells = models.BigIntegerField(db_column='Esophageal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_aortic_adventitial = models.BigIntegerField(db_column='Fibroblast - Aortic Adventitial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_cardiac = models.BigIntegerField(db_column='Fibroblast - Cardiac', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_choroid_plexus = models.BigIntegerField(db_column='Fibroblast - Choroid Plexus', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_conjunctival = models.BigIntegerField(db_column='Fibroblast - Conjunctival', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_dermal = models.BigIntegerField(db_column='Fibroblast - Dermal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_gingival = models.BigIntegerField(db_column='Fibroblast - Gingival', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_lung = models.BigIntegerField(db_column='Fibroblast - Lung', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_lymphatic = models.BigIntegerField(db_column='Fibroblast - Lymphatic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_mammary = models.BigIntegerField(db_column='Fibroblast - Mammary', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_periodontal_ligament = models.BigIntegerField(db_column='Fibroblast - Periodontal Ligament', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_pulmonary_artery = models.BigIntegerField(db_column='Fibroblast - Pulmonary Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_skin = models.BigIntegerField(db_column='Fibroblast - skin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fibroblast_villous_mesenchymal = models.BigIntegerField(db_column='Fibroblast - Villous Mesenchymal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gamma_delta_positive_t_cells = models.BigIntegerField(db_column='gamma delta positive T cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gingival_epithelial_cells = models.BigIntegerField(db_column='Gingival epithelial cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    granulocyte_macrophage_progenitor = models.BigIntegerField(db_column='granulocyte macrophage progenitor', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hair_follicle_dermal_papilla_cells = models.BigIntegerField(db_column='Hair Follicle Dermal Papilla Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hair_follicle_outer_root_sheath_cells = models.BigIntegerField(db_column='Hair Follicle Outer Root Sheath Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hepatic_sinusoidal_endothelial_cells = models.BigIntegerField(db_column='Hepatic Sinusoidal Endothelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hepatic_stellate_cells_lipocyte_field = models.BigIntegerField(db_column='Hepatic Stellate Cells (lipocyte)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hepatocyte = models.BigIntegerField(db_column='Hepatocyte', blank=True, null=True)  # Field name made lowercase.
    immature_langerhans_cells = models.BigIntegerField(db_column='immature langerhans cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    intestinal_epithelial_cells_polarized_field = models.BigIntegerField(db_column='Intestinal epithelial cells (polarized)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    iris_pigment_epithelial_cells = models.BigIntegerField(db_column='Iris Pigment Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keratinocyte_epidermal = models.BigIntegerField(db_column='Keratinocyte - epidermal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keratinocyte_oral = models.BigIntegerField(db_column='Keratinocyte - oral', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    keratocytes = models.BigIntegerField(db_column='Keratocytes', blank=True, null=True)  # Field name made lowercase.
    lens_epithelial_cells = models.BigIntegerField(db_column='Lens Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    macrophage_monocyte_derived = models.BigIntegerField(db_column='Macrophage - monocyte derived', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mallassez_derived_cells = models.BigIntegerField(db_column='Mallassez-derived cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mammary_epithelial_cell = models.BigIntegerField(db_column='Mammary Epithelial Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mast_cell = models.BigIntegerField(db_column='Mast cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mature_adipocyte = models.BigIntegerField(db_column='mature adipocyte', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    melanocyte = models.BigIntegerField(db_column='Melanocyte', blank=True, null=True)  # Field name made lowercase.
    meningeal_cells = models.BigIntegerField(db_column='Meningeal Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_precursor_cell_adipose = models.BigIntegerField(db_column='mesenchymal precursor cell - adipose', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mesenchymal_precursor_cell_bone_marrow = models.BigIntegerField(db_column='mesenchymal precursor cell - bone marrow', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mesenchymal_precursor_cell_cardiac = models.BigIntegerField(db_column='mesenchymal precursor cell - cardiac', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_adipose = models.BigIntegerField(db_column='Mesenchymal stem cells - adipose', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_amniotic_membrane = models.BigIntegerField(db_column='Mesenchymal Stem Cells - amniotic membrane', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_bone_marrow = models.BigIntegerField(db_column='Mesenchymal Stem Cells - bone marrow', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_hepatic = models.BigIntegerField(db_column='Mesenchymal stem cells - hepatic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_umbilical = models.BigIntegerField(db_column='Mesenchymal stem cells - umbilical', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_vertebral = models.BigIntegerField(db_column='Mesenchymal Stem Cells - Vertebral', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesenchymal_stem_cells_wharton_jelly = models.BigIntegerField(db_column='Mesenchymal Stem Cells - Wharton Jelly', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mesothelial_cells = models.BigIntegerField(db_column='Mesothelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    migratory_langerhans_cells = models.BigIntegerField(db_column='migratory langerhans cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    multipotent_cord_blood_unrestricted_somatic_stem_cells = models.BigIntegerField(db_column='Multipotent Cord Blood Unrestricted Somatic Stem Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    myoblast = models.BigIntegerField(db_column='Myoblast', blank=True, null=True)  # Field name made lowercase.
    nasal_epithelial_cells = models.BigIntegerField(db_column='nasal epithelial cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    natural_killer_cells = models.BigIntegerField(db_column='Natural Killer Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    neural_stem_cells = models.BigIntegerField(db_column='Neural stem cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    neurons = models.BigIntegerField(db_column='Neurons', blank=True, null=True)  # Field name made lowercase.
    neutrophil = models.BigIntegerField(db_column='Neutrophil', blank=True, null=True)  # Field name made lowercase.
    nucleus_pulposus_cell = models.BigIntegerField(db_column='Nucleus Pulposus Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    olfactory_epithelial_cells = models.BigIntegerField(db_column='Olfactory epithelial cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oligodendrocyte_precursors = models.BigIntegerField(db_column='Oligodendrocyte - precursors', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    osteoblast = models.BigIntegerField(db_column='Osteoblast', blank=True, null=True)  # Field name made lowercase.
    pancreatic_stromal_cells = models.BigIntegerField(db_column='Pancreatic stromal cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pericytes = models.BigIntegerField(db_column='Pericytes', blank=True, null=True)  # Field name made lowercase.
    perineurial_cells = models.BigIntegerField(db_column='Perineurial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    placental_epithelial_cells = models.BigIntegerField(db_column='Placental Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_breast = models.BigIntegerField(db_column='Preadipocyte - breast', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_omental = models.BigIntegerField(db_column='Preadipocyte - omental', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_perirenal = models.BigIntegerField(db_column='Preadipocyte - perirenal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_subcutaneous = models.BigIntegerField(db_column='Preadipocyte - subcutaneous', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    preadipocyte_visceral = models.BigIntegerField(db_column='Preadipocyte - visceral', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    promyelocytes = models.BigIntegerField(blank=True, null=True)
    prostate_epithelial_cells = models.BigIntegerField(db_column='Prostate Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prostate_stromal_cells = models.BigIntegerField(db_column='Prostate Stromal Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_cortical_epithelial_cells = models.BigIntegerField(db_column='Renal Cortical Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_epithelial_cells = models.BigIntegerField(db_column='Renal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_glomerular_endothelial_cells = models.BigIntegerField(db_column='Renal Glomerular Endothelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_mesangial_cells = models.BigIntegerField(db_column='Renal Mesangial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    renal_proximal_tubular_epithelial_cell = models.BigIntegerField(db_column='Renal Proximal Tubular Epithelial Cell', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    retinal_pigment_epithelial_cells = models.BigIntegerField(db_column='Retinal Pigment Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salivary_acinar_cells = models.BigIntegerField(db_column='salivary acinar cells', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    schwann_cells = models.BigIntegerField(db_column='Schwann Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sebocyte = models.BigIntegerField(db_column='Sebocyte', blank=True, null=True)  # Field name made lowercase.
    sertoli_cells = models.BigIntegerField(db_column='Sertoli Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skeletal_muscle_cells = models.BigIntegerField(db_column='Skeletal Muscle Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skeletal_muscle_cells_differentiated_into_myotubes = models.BigIntegerField(db_column='Skeletal muscle cells differentiated into Myotubes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    skeletal_muscle_satellite_cells = models.BigIntegerField(db_column='Skeletal Muscle Satellite Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    small_airway_epithelial_cells = models.BigIntegerField(db_column='Small Airway Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_airway = models.BigIntegerField(db_column='Smooth muscle cells - airway', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_aortic = models.BigIntegerField(db_column='Smooth Muscle Cells - Aortic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_bladder = models.BigIntegerField(db_column='Smooth Muscle Cells - Bladder', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_brachiocephalic = models.BigIntegerField(db_column='Smooth Muscle Cells - Brachiocephalic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_brain_vascular = models.BigIntegerField(db_column='Smooth Muscle Cells - Brain Vascular', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_bronchial = models.BigIntegerField(db_column='Smooth Muscle Cells - Bronchial', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_carotid = models.BigIntegerField(db_column='Smooth Muscle Cells - Carotid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_colonic = models.BigIntegerField(db_column='Smooth Muscle Cells - Colonic', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_coronary_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Coronary Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_esophageal = models.BigIntegerField(db_column='Smooth Muscle Cells - Esophageal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_internal_thoracic_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Internal Thoracic Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_intestinal = models.BigIntegerField(db_column='Smooth Muscle Cells - Intestinal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_prostate = models.BigIntegerField(db_column='Smooth Muscle Cells - Prostate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_pulmonary_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Pulmonary Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_subclavian_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Subclavian Artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_tracheal = models.BigIntegerField(db_column='Smooth Muscle Cells - Tracheal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_umbilical_artery = models.BigIntegerField(db_column='Smooth Muscle Cells - Umbilical artery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_umbilical_vein = models.BigIntegerField(db_column='Smooth Muscle Cells - Umbilical Vein', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    smooth_muscle_cells_uterine = models.BigIntegerField(db_column='Smooth Muscle Cells - Uterine', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    synoviocyte = models.BigIntegerField(db_column='Synoviocyte', blank=True, null=True)  # Field name made lowercase.
    tenocyte = models.BigIntegerField(blank=True, null=True)
    trabecular_meshwork_cells = models.BigIntegerField(db_column='Trabecular Meshwork Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tracheal_epithelial_cells = models.BigIntegerField(db_column='Tracheal Epithelial Cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urothelial_cells = models.BigIntegerField(db_column='Urothelial cells', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    objects = models.Manager()
    pdobjects = DataFrameManager()  # Pandas-Enabled Manager

    class Meta:
        managed = False
        db_table = 'enhancers_154cells_binarized'
