"""empty message

Revision ID: c1f0bab1178f
Revises: 
Create Date: 2022-02-03 11:21:13.069391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1f0bab1178f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('query_id', sa.String(length=16), nullable=True),
    sa.Column('homologs', sa.Text(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_alignment')),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id', name=op.f('uq_alignment_id'))
    )
    with op.batch_alter_table('alignment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_alignment_query_id'), ['query_id'], unique=True)

    op.create_table('operator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number_seqs', sa.Integer(), nullable=True),
    sa.Column('consensus_score', sa.Float(precision=128), nullable=True),
    sa.Column('validated', sa.Boolean(), nullable=True),
    sa.Column('motif', sa.Text(length=4096), nullable=True),
    sa.Column('aligned_seqs', sa.Text(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_operator')),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id', name=op.f('uq_operator_id'))
    )
    op.create_table('operon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('operon_seq', sa.String(length=4096), nullable=True),
    sa.Column('operon', sa.Text(length=4096), nullable=True),
    sa.Column('genome_id', sa.String(length=16), nullable=True),
    sa.Column('start_pos', sa.Integer(), nullable=True),
    sa.Column('stop_pos', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_operon')),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id', name=op.f('uq_operon_id'))
    )
    op.create_table('regulator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prot_id', sa.String(length=16), nullable=True),
    sa.Column('genome_id', sa.String(length=16), nullable=True),
    sa.Column('organism', sa.String(length=128), nullable=True),
    sa.Column('start_pos', sa.Integer(), nullable=True),
    sa.Column('stop_pos', sa.Integer(), nullable=True),
    sa.Column('strand', sa.String(length=4), nullable=True),
    sa.Column('organism_id', sa.Integer(), nullable=True),
    sa.Column('operator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['operator_id'], ['operator.id'], name=op.f('fk_regulator_operator_id_operator')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_regulator')),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id', name=op.f('uq_regulator_id'))
    )
    with op.batch_alter_table('regulator', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_regulator_prot_id'), ['prot_id'], unique=True)

    op.create_table('association',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('regulator_id', sa.Integer(), nullable=True),
    sa.Column('operon_id', sa.Integer(), nullable=True),
    sa.Column('reg_index', sa.Integer(), nullable=True),
    sa.Column('reg_type', sa.Integer(), nullable=True),
    sa.Column('regulated_seq', sa.String(length=4096), nullable=True),
    sa.ForeignKeyConstraint(['operon_id'], ['operon.id'], name=op.f('fk_association_operon_id_operon')),
    sa.ForeignKeyConstraint(['regulator_id'], ['regulator.id'], name=op.f('fk_association_regulator_id_regulator')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_association')),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('id', name=op.f('uq_association_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    with op.batch_alter_table('regulator', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_regulator_prot_id'))

    op.drop_table('regulator')
    op.drop_table('operon')
    op.drop_table('operator')
    with op.batch_alter_table('alignment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_alignment_query_id'))

    op.drop_table('alignment')
    # ### end Alembic commands ###
