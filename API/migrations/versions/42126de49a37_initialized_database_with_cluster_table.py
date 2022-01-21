"""initialized database with Cluster table

Revision ID: 42126de49a37
Revises: 
Create Date: 2021-11-15 09:13:27.542285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42126de49a37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cluster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('family', sa.String(length=16), nullable=True),
    sa.Column('cluster_percent_identity', sa.Integer(), nullable=True),
    sa.Column('rep_EMBL', sa.String(length=16), nullable=True),
    sa.Column('rep_genome', sa.String(length=16), nullable=True),
    sa.Column('rep_operon', sa.PickleType(), nullable=True),
    sa.Column('reg_index', sa.Integer(), nullable=True),
    sa.Column('rep_ligand_SMILES', sa.String(length=256), nullable=True),
    sa.Column('rep_ligand_NAME', sa.String(length=256), nullable=True),
    sa.Column('homologs', sa.PickleType(), nullable=True),
    sa.Column('dna_binding_motif', sa.PickleType(), nullable=True),
    sa.Column('ligand_binding_motif', sa.PickleType(), nullable=True),
    sa.Column('gene_context_motif', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cluster_cluster_percent_identity'), 'cluster', ['cluster_percent_identity'], unique=False)
    op.create_index(op.f('ix_cluster_family'), 'cluster', ['family'], unique=False)
    op.create_index(op.f('ix_cluster_reg_index'), 'cluster', ['reg_index'], unique=False)
    op.create_index(op.f('ix_cluster_rep_EMBL'), 'cluster', ['rep_EMBL'], unique=True)
    op.create_index(op.f('ix_cluster_rep_genome'), 'cluster', ['rep_genome'], unique=False)
    op.create_index(op.f('ix_cluster_rep_ligand_NAME'), 'cluster', ['rep_ligand_NAME'], unique=False)
    op.create_index(op.f('ix_cluster_rep_ligand_SMILES'), 'cluster', ['rep_ligand_SMILES'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cluster_rep_ligand_SMILES'), table_name='cluster')
    op.drop_index(op.f('ix_cluster_rep_ligand_NAME'), table_name='cluster')
    op.drop_index(op.f('ix_cluster_rep_genome'), table_name='cluster')
    op.drop_index(op.f('ix_cluster_rep_EMBL'), table_name='cluster')
    op.drop_index(op.f('ix_cluster_reg_index'), table_name='cluster')
    op.drop_index(op.f('ix_cluster_family'), table_name='cluster')
    op.drop_index(op.f('ix_cluster_cluster_percent_identity'), table_name='cluster')
    op.drop_table('cluster')
    # ### end Alembic commands ###