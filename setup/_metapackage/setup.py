import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-crm",
    description="Meta package for oca-crm Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-crm_claim',
        'odoo12-addon-crm_claim_code',
        'odoo12-addon-crm_lead_code',
        'odoo12-addon-crm_lead_firstname',
        'odoo12-addon-crm_lead_product',
        'odoo12-addon-crm_phonecall',
        'odoo12-addon-crm_phonecall_summary_predefined',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
