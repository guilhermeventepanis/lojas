select * 
from clientes cc
inner join contato_cl cl
on cc.cliente_id = cl.cliente_id
inner join enderecos_clientes ec
on cc.cliente_id = ec.cliente_id;

select * from produtos; 

select * 
from clientes cl
inner join pedido pd
on cl.cliente_id = pd.cliente_id
inner join produtos ps
on pd.produto_id = ps.produto_id; 

select * 
from fornecedores fd
inner join material_fornecedor mf
on fd.mf_id = mf.mf_id
inner join enderecos ed
on fd.fornecedor_id = ed.fornecedor_id
inner join contato_fn cfn
on fd.fornecedor_id = cfn.fornecedor_id;
