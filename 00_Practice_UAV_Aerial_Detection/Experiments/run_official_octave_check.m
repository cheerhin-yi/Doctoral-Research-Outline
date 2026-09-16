function run_official_octave_check(repoDir, outputDir)
% Run the unchanged A0-07 harness with original VisDrone code under Octave.
% Use a new output directory per attempt; no real images or predictions.
assert(exist('OCTAVE_VERSION', 'builtin') ~= 0, 'This wrapper records Octave compatibility only');
assert(exist(outputDir, 'dir') == 0, 'Output directory already exists');
mkdir(outputDir);
diary(fullfile(outputDir, 'octave.log'));
meta = struct('runtime', 'GNU Octave', 'version', version(), ...
    'matlab_executed', false, 'model_executed', false, 'passed', false);
try
    pkg('load', 'image');
    fixtureDir = fullfile(repoDir, '11_Datasets', 'processed', 'VisDrone', 'A0-07', 'probe_02');
    toolkitDir = fullfile(repoDir, '11_Datasets', 'processed', 'VisDrone', ...
        'Official_Runtime_Check_2026-09-11', 'toolkit', 'VisDrone2018-DET-toolkit-master');
    addpath(fixtureDir);
    addpath(fullfile(toolkitDir, 'utils'));
    meta.mean2_path = which('mean2');
    meta.calcAccuracy_path = which('calcAccuracy');
    meta.evalRes_path = which('evalRes');
    meta.harness_path = which('run_a007_official');
    meta.packages = pkg('list');
    results = run_a007_official(toolkitDir, fullfile(outputDir, 'original_save.mat'));
    meta.case_count = numel(fieldnames(results));
    assert(meta.case_count == 24, 'Incomplete harness result');
    save('-mat7-binary', fullfile(outputDir, 'results_matlab_format.mat'), 'results');
    write_json(fullfile(outputDir, 'actual.json'), results);
    meta.passed = true;
    write_json(fullfile(outputDir, 'runtime.json'), meta);
    fprintf('Completed %d original-harness assertions under Octave %s.\n', meta.case_count, version());
catch err
    meta.error = err.message;
    meta.stack = err.stack;
    write_json(fullfile(outputDir, 'runtime.json'), meta);
    fprintf(2, 'Cross-runtime check failed: %s\n', err.message);
    diary off;
    rethrow(err);
end
diary off;
end

function write_json(path, data)
fid = fopen(path, 'w');
assert(fid ~= -1, 'Cannot open JSON output');
cleanup = onCleanup(@() fclose(fid));
fprintf(fid, '%s\n', jsonencode(data));
end
