$(document).ready(function() {
    $(".right-panel").prepend(`
        <div class="card">
            <div class="card-content">
                <a href="/dashboard/usuarios/egresado/import/" class="btn btn-primary import">Importar</a>
                <a target="_blank" href="/usuarios/export/xls/" class="btn btn-primary import">Exportar</a>
            </div>
        </div>`);
    $('select').material_select();
});
